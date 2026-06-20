# Refinery Run — Night Shift Automated Script
# Schedule: 3:00 AM daily via Windows Task Scheduler
# Mission: Extract atomic notes from literature notes

param(
    [string]$VaultPath = "E:\_Knowledge\ObsidianVault",
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$Date = Get-Date -Format "yyyy-MM-dd"

Write-Host "=== Refinery Run — $Timestamp ===" -ForegroundColor Cyan

# Ensure directories exist
$Directories = @(
    "$VaultPath\2-atoms\concepts",
    "$VaultPath\2-atoms\people",
    "$VaultPath\2-atoms\events",
    "$VaultPath\sources\archived",
    "$VaultPath\3-threads\_friction",
    "$VaultPath\1-desk\_needs-work",
    "$VaultPath\briefings"
)

foreach ($Dir in $Directories) {
    if (!(Test-Path $Dir)) {
        New-Item -ItemType Directory -Path $Dir -Force | Out-Null
        Write-Host "Created: $Dir" -ForegroundColor Gray
    }
}

# Track statistics
$Stats = @{
    Processed = 0
    AtomsCreated = 0
    SourcesArchived = 0
    Skipped = 0
    NeedsWork = 0
    FrictionFlags = 0
}

$NewAtoms = @()
$FrictionFlags = @()

# Function to extract claims from literature note
function Extract-Claims {
    param([string]$Content)

    $Claims = @()

    # Look for bullet points with claims
    $Lines = $Content -split "`n"
    foreach ($Line in $Lines) {
        if ($Line -match "^[-*•]\s*(.+(?:claim|found|study|research|evidence|shows|found|according).+)" -or
            $Line -match "^[-*•]\s*\[.+\]\s*(.+)") {
            $Claims += $Matches[1].Trim()
        }
    }

    # Look for numbered claims
    if ($Content -match "(?<=\n)(\d+\. .{20,})") {
        $Claims += $Matches[0].Trim()
    }

    return $Claims
}

# Function to generate atomic note from claim
function New-AtomicNote {
    param(
        [string]$Concept,
        [string]$Content,
        [hashtable]$Metadata,
        [string]$SourceType,
        [string]$LiteratureNotePath
    )

    # Clean concept name for filename
    $CleanConcept = $Concept -replace '[^\w\s-]', '' -replace '\s+', ' '
    $FileName = "$CleanConcept.md"

    # Determine category
    $Category = "concepts"
    if ($Concept -match "(person|researcher|author|founder|leader)$" -or
        $Concept -match "^[A-Z]\. [A-Z]\.|^[A-Z][a-z]+ [A-Z][a-z]+") {
        $Category = "people"
    }

    $OutputPath = "$VaultPath\2-atoms\$Category\$FileName"

    # Check if note already exists (avoid duplicates)
    if (Test-Path $OutputPath) {
        Write-Host "  Skip: $Concept (already exists)" -ForegroundColor Gray
        $Stats.Skipped++
        return $null
    }

    # Quality gate checks
    $QualityIssues = @()

    if ([string]::IsNullOrWhiteSpace($Metadata.Source)) {
        $QualityIssues += "Missing source citation"
    }

    if ($Concept.Length -lt 3 -or $Concept.Length -gt 80) {
        $QualityIssues += "Concept name too short/long"
    }

    # If quality issues, move to needs-work
    if ($QualityIssues.Count -gt 0) {
        $NeedsWorkPath = "$VaultPath\1-desk\_needs-work\$Date — $CleanConcept.md"
        $NeedsWorkContent = @"
# $Concept

## Needs Work
$($QualityIssues -join "`n")

## Original Content
$Content

## Source
$($Metadata.Source)
"@
        if (!$DryRun) {
            Set-Content -Path $NeedsWorkPath -Value $NeedsWorkContent -Encoding UTF8
        }
        $Stats.NeedsWork++
        return $null
    }

    # Confidence level based on source type
    $Confidence = "stated"
    if ($SourceType -eq "blog" -or $SourceType -eq "twitter") {
        $Confidence = "speculation"
    }

    # Generate frontmatter
    $Tags = "concept"
    if ($Category -eq "people") { $Tags = "person" }

    $Frontmatter = @"
---
date: $Date
type: permanent
tags: [$Tags]
ai-first: true
source: $([System.IO.Path]::GetFileNameWithoutExtension($LiteratureNotePath))
---

## For future Claude
This note explains $Concept extracted on $Date from $([System.IO.Path]::GetFileNameWithoutExtension($LiteratureNotePath)). It covers one atomic idea from the source material.

## $Concept

$Content

**Key claim:** $Concept (as of $Date, $Confidence in $($Metadata.Source))

## Evidence
> Extracted from literature note: $([System.IO.Path]::GetFileNameWithoutExtension($LiteratureNotePath))

## Links
- Related: [[Digital Garden]], [[Knowledge Management]]
- Builds on: [[Evergreen Content]]

## Confidence
$Confidence

## Metadata
- Extracted from: $([System.IO.Path]::GetFileNameWithoutExtension($LiteratureNotePath))
- Raw source: $($Metadata.Source)
- Extracted by: Refinery Run, $Timestamp
"@

    if (!$DryRun) {
        Set-Content -Path $OutputPath -Value $Frontmatter -Encoding UTF8
        Write-Host "  Created: $OutputPath" -ForegroundColor Green
        $Stats.AtomsCreated++
        $NewAtoms += @{
            Path = $OutputPath
            Concept = $Concept
            Summary = $Content.Substring(0, [Math]::Min(50, $Content.Length))
        }
    } else {
        Write-Host "  [DRY RUN] Would create: $OutputPath" -ForegroundColor Yellow
    }

    return $OutputPath
}

# Process literature notes from 1-desk
Write-Host "`nProcessing 1-desk/..." -ForegroundColor Magenta

$DeskPath = "$VaultPath\1-desk"
if (Test-Path $DeskPath) {
    $Subdirs = Get-ChildItem -Path $DeskPath -Directory |
        Where-Object { $_.Name -notlike "_*" }

    foreach ($Subdir in $Subdirs) {
        Write-Host "`n  Subdir: $($Subdir.Name)" -ForegroundColor Cyan

        $Files = Get-ChildItem -Path $Subdir.FullName -Filter "*.md" |
            Where-Object {
                $Content = Get-Content $_.FullName -Raw
                $Content -match "status:\s*to-process"
            }

        foreach ($File in $Files) {
            Write-Host "    Processing: $($File.Name)" -ForegroundColor Gray

            $Content = Get-Content $File.FullName -Raw

            # Extract frontmatter metadata
            $FrontmatterMatch = $Content -match "(?s)^---(.+?)---"
            if (!$FrontmatterMatch) {
                Write-Host "    Skip: No frontmatter" -ForegroundColor Yellow
                $Stats.Skipped++
                continue
            }

            $Frontmatter = $Matches[1]
            $Subtype = "article"
            $Source = ""
            $Author = ""

            if ($Frontmatter -match "subtype:\s*(.+)") { $Subtype = $Matches[1].Trim() }
            if ($Frontmatter -match "source:\s*(.+)") { $Source = $Matches[1].Trim() }
            if ($Frontmatter -match "author:\s*(.+)") { $Author = $Matches[1].Trim() }

            # Extract body content (after frontmatter)
            $BodyStart = $Content.IndexOf("`n`n", $Content.IndexOf("---`n") + 3) + 2
            $Body = $Content.Substring($BodyStart)

            # Extract claims/concepts to atomize
            $Claims = Extract-Claims -Content $Body

            if ($Claims.Count -eq 0) {
                # Try to extract section headers as concepts
                if ($Body -match "##\s+(.+)") {
                    $Claims = $Matches[1]
                }
            }

            foreach ($Claim in $Claims) {
                # Extract concept from claim
                $Concept = $Claim

                # Simplify concept name
                if ($Concept -match "^(.{30,}?)\s+(?:is|means|refers to|defines)") {
                    $Concept = $Matches[1]
                }

                # Create atomic note
                $AtomPath = New-AtomicNote `
                    -Concept $Concept `
                    -Content $Claim `
                    -Metadata @{ Source = $Source; Author = $Author } `
                    -SourceType $Subtype `
                    -LiteratureNotePath $File.FullName

                if ($AtomPath) {
                    $Stats.Processed++
                }
            }

            # Archive the source literature note
            $ArchiveName = "$Date — $($File.Name)"
            $ArchivePath = "$VaultPath\sources\archived\$ArchiveName"

            if (!$DryRun) {
                # Update status in archived note
                $ArchivedContent = $Content -replace "status:\s*to-process", "status: processed"
                $ArchivedContent += @"

## Extraction Log
- **Date:** $Timestamp
- **Refinery Run:** Extracted $($Claims.Count) atomic notes
- **Atoms created:** $($Claims.Count)
"@
                Move-Item -Path $File.FullName -Destination $ArchivePath -Force
                Set-Content -Path $ArchivePath -Value $ArchivedContent -Encoding UTF8
                Write-Host "    Archived: $ArchiveName" -ForegroundColor Gray
                $Stats.SourcesArchived++
            } else {
                Write-Host "    [DRY RUN] Would archive: $ArchiveName" -ForegroundColor Yellow
            }
        }
    }
}

# Update log.md
Write-Host "`nUpdating log.md..." -ForegroundColor Magenta
$LogEntry = @"

## [$Timestamp] Refinery Run | Extracted $($Stats.AtomsCreated) atoms
- Processed: $($Stats.Processed) literature notes from `1-desk/`
- Created: $($Stats.AtomsCreated) atomic notes in `2-atoms/`
- Archived: $($Stats.SourcesArchived) sources to `sources/archived/`
- Skipped: $($Stats.Skipped) items (already processed/missing source)
- Needs work: $($Stats.NeedsWork) atoms (check `1-desk/_needs-work/`)
- [FRICTION] flags: $($Stats.FrictionFlags) conflicts detected (passed to Editor)
"@

if (!$DryRun) {
    Add-Content -Path "$VaultPath\log.md" -Value $LogEntry -Encoding UTF8
} else {
    Write-Host "  [DRY RUN] Would append to log.md" -ForegroundColor Yellow
}

# Generate morning brief section
Write-Host "Generating morning brief section..." -ForegroundColor Magenta
$BriefPath = "$VaultPath\briefings\$Date — Morning Brief.md"

$BriefSection = @"

---

## Refinery Run Summary — $Timestamp

**Extraction:**
- Processed: $($Stats.Processed) literature notes
- Created: $($Stats.AtomsCreated) atomic notes
- Archived: $($Stats.SourcesArchived) sources
- Skipped: $($Stats.Skipped) (missing source/already done)
- Needs work: $($Stats.NeedsWork) atoms (check `1-desk/_needs-work/`)

**New Atomic Notes:**
"@

foreach ($Atom in $NewAtoms) {
    $AtomName = [System.IO.Path]::GetFileNameWithoutExtension($Atom.Path)
    $BriefSection += "`n1. [[$AtomName]] — $($Atom.Summary)"
}

if ($Stats.FrictionFlags -gt 0) {
    $BriefSection += "`n`n**[FRICTION] Flags (needs your review):**`n"
    foreach ($Flag in $FrictionFlags) {
        $BriefSection += "`n1. `3-threads/_friction\$($Flag.File)` — $($Flag.Description)"
    }
}

$BriefSection += @"

**Action Needed:**
- [ ] Skim new atoms for drift (spot-check 2-3)
- [ ] Resolve [FRICTION] conflicts
- [ ] Review `_needs-work/` items

---
*Refinery Run section — $Timestamp*
"@

if (!$DryRun) {
    if (Test-Path $BriefPath) {
        # Append to existing brief
        Add-Content -Path $BriefPath -Value $BriefSection -Encoding UTF8
    } else {
        # Create new brief with just refinery section
        $FullBrief = @"
---
date: $Date
type: daily-briefing
tags: [morning-brief, refinery-output]
ai-first: true
---

# Morning Brief — $Date
$BriefSection
"@
        Set-Content -Path $BriefPath -Value $FullBrief -Encoding UTF8
    }
    Write-Host "  Updated: $BriefPath" -ForegroundColor Green
} else {
    Write-Host "  [DRY RUN] Would update: $BriefPath" -ForegroundColor Yellow
}

# Summary
Write-Host "`n=== Refinery Run Complete ===" -ForegroundColor Cyan
Write-Host "Atoms Created: $($Stats.AtomsCreated)" -ForegroundColor White
Write-Host "Sources Archived: $($Stats.SourcesArchived)" -ForegroundColor Gray
Write-Host "Duration: $([Math]::Round((Get-Date - $StartTime).TotalSeconds, 1)) seconds" -ForegroundColor Gray