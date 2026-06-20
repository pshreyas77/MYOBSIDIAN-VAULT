# Editor Run — Night Shift Automated Script
# Schedule: 6:00 AM daily via Windows Task Scheduler
# Mission: Link atomic notes, detect contradictions, update index

param(
    [string]$VaultPath = "E:\_Knowledge\ObsidianVault",
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$Date = Get-Date -Format "yyyy-MM-dd"

Write-Host "=== Editor Run — $Timestamp ===" -ForegroundColor Cyan

# Track statistics
$Stats = @{
    AtomsProcessed = 0
    OutgoingLinks = 0
    IncomingLinks = 0
    FrictionFlags = 0
    IndexUpdates = 0
    OrphansFound = 0
}

$NewAtoms = @()
$FrictionBlocks = @()
$IndexEntries = @()

# Function to find related notes in vault
function Find-RelatedNotes {
    param(
        [string]$Concept,
        [int]$Limit = 5
    )

    $Related = @()
    $VaultMd = Get-ChildItem -Path $VaultPath -Filter "*.md" -Recurse |
        Where-Object { $_.FullName -notmatch "\\(0-raw|00 - INBOX|_quarantine|_needs-work)\\$" }

    # Search by title similarity
    foreach ($File in $VaultMd) {
        $Title = [System.IO.Path]::GetFileNameWithoutExtension($File.Name)
        if ($Title -like "*$Concept*" -or $Concept -like "*$Title*") {
            $Related += @{
                Path = $File.FullName
                Title = $Title
                Reason = "Title match"
            }
        }

        if ($Related.Count -ge $Limit) { break }
    }

    # Search by content if not enough matches
    if ($Related.Count -lt 3) {
        foreach ($File in $VaultMd) {
            try {
                $Content = Get-Content $File.FullName -Raw -ErrorAction SilentlyContinue
                if ($Content -match [regex]::Escape($Concept)) {
                    $Title = [System.IO.Path]::GetFileNameWithoutExtension($File.Name)
                    if ($Related.Title -notcontains $Title) {
                        $Related += @{
                            Path = $File.FullName
                            Title = $Title
                            Reason = "Content match"
                        }
                    }
                }
            } catch { continue }

            if ($Related.Count -ge $Limit) { break }
        }
    }

    return $Related
}

# Function to detect contradictions
function Test-Friction {
    param(
        [string]$NewAtomPath,
        [string]$Concept
    )

    $Content = Get-Content $NewAtomPath -Raw
    $FrictionDetected = $false

    # Look for contradiction patterns
    $ContradictionPatterns = @(
        "(?:but|however|although|while|contrary to|despite)\s+(?:the\s+)?(?:fact\s+)?(?:that\s+)?(?:previous|earlier|old|traditional)",
        "(?:is\s+no\s+longer|has\s+changed|updated\s+view|new\s+evidence)",
        "(?:conflicts?|contradicts?|challenges?|questions?|debunks?)"
    )

    foreach ($Pattern in $ContradictionPatterns) {
        if ($Content -match $Pattern) {
            $FrictionDetected = $true
            break
        }
    }

    return $FrictionDetected
}

# Function to create friction block
function New-FrictionBlock {
    param(
        [string]$Concept,
        [string]$NoteA,
        [string]$NoteB,
        [string]$Conflict
    )

    $FileName = "$Date — $Concept Conflict.md"
    $OutputPath = "$VaultPath\3-threads\_friction\$FileName"

    $Frontmatter = @"
---
date: $Date
type: friction
tags: [contradiction, needs-review]
ai-first: true
related: [[$NoteA], [$NoteB]]
---

## [FRICTION] — $Concept Contradiction

**Detection phase:** Editor Run, $Timestamp

**Side A:**
- Note: [[$NoteA]]
- Claim: Pending review

**Side B:**
- Note: [[$NoteB]]
- Claim: Pending review

**Conflict:**
$Conflict

**Possible resolutions:**
1. Temporal update (claim changed between dates)
2. Contextual difference (true in A, false in B)
3. One source is unreliable
4. Both are right in different senses

**Action:**
- [ ] Read both notes fully
- [ ] Check source dates and credibility
- [ ] Update or archive outdated claim
- [ ] Delete this friction note once resolved

---
*Created by Editor Run — $Timestamp*
"@

    if (!$DryRun) {
        Set-Content -Path $OutputPath -Value $Frontmatter -Encoding UTF8
        Write-Host "  [FRICTION] Created: $FileName" -ForegroundColor Red
        $Stats.FrictionFlags++
        $FrictionBlocks += @{
            File = $FileName
            Description = "$NoteA vs $NoteB"
        }
    } else {
        Write-Host "  [DRY RUN] Would create friction: $FileName" -ForegroundColor Yellow
    }

    return $OutputPath
}

# Process new atoms from 2-atoms
Write-Host "`nProcessing 2-atoms/..." -ForegroundColor Magenta

$AtomsPath = "$VaultPath\2-atoms"
if (Test-Path $AtomsPath) {
    $Categories = Get-ChildItem -Path $AtomsPath -Directory

    foreach ($Category in $Categories) {
        Write-Host "`n  Category: $($Category.Name)" -ForegroundColor Cyan

        # Find new atoms (modified in last 24 hours)
        $Files = Get-ChildItem -Path $Category.FullName -Filter "*.md" |
            Where-Object { $_.LastWriteTime -gt (Get-Date).AddHours(-24) }

        foreach ($File in $Files) {
            Write-Host "    Processing: $($File.Name)" -ForegroundColor Gray

            $Content = Get-Content $File.FullName -Raw
            $Concept = [System.IO.Path]::GetFileNameWithoutExtension($File.Name)

            # Find related notes for linking
            $Related = Find-RelatedNotes -Concept $Concept -Limit 5

            if ($Related.Count -gt 0) {
                # Add outgoing links to the atom
                $LinksSection = @"

## Links (Added by Editor Run)
"@

                foreach ($Rel in $Related) {
                    $LinksSection += "`n- Related: [[$($Rel.Title)]] — $($Rel.Reason)"
                    $Stats.OutgoingLinks++
                }

                # Append links to atom
                if (!$DryRun) {
                    $UpdatedContent = $Content + $LinksSection
                    Set-Content -Path $File.FullName -Value $UpdatedContent -Encoding UTF8
                }
            }

            # Add backlinks from related notes
            foreach ($Rel in $Related) {
                try {
                    $RelContent = Get-Content $Rel.Path -Raw
                    $Backlink = "`n- See also: [[$Concept]] — Added by Editor Run, $Date"

                    if ($RelContent -notmatch "\[\[$Concept\]\]") {
                        $UpdatedRelContent = $RelContent + $Backlink
                        if (!$DryRun) {
                            Set-Content -Path $Rel.Path -Value $UpdatedRelContent -Encoding UTF8
                            Write-Host "      Added backlink from: $($Rel.Title)" -ForegroundColor Gray
                            $Stats.IncomingLinks++
                        }
                    }
                } catch { continue }
            }

            # Check for friction/contradictions
            if (Test-Friction -NewAtomPath $File.FullName -Concept $Concept) {
                $RelatedConcepts = $Related | Select-Object -First 1
                if ($RelatedConcepts) {
                    New-FrictionBlock -Concept $Concept -NoteA $Concept -NoteB $RelatedConcepts.Title -Conflict "Potential contradiction detected during Editor Run"
                }
            }

            # Track for index
            $IndexEntries += @{
                Concept = $Concept
                Category = $Category.Name
                Path = $File.FullName
                Date = $Date
            }

            $NewAtoms += $File
            $Stats.AtomsProcessed++
        }
    }
}

# Update index.md
Write-Host "`nUpdating index.md..." -ForegroundColor Magenta
$IndexPath = "$VaultPath\index.md"

if (Test-Path $IndexPath) {
    $IndexContent = Get-Content $IndexPath -Raw

    foreach ($Entry in $IndexEntries) {
        $IndexLine = "- `2-atoms/$($Entry.Category)/$($Entry.Concept).md` — auto-indexed ($($Entry.Date))`n"

        # Find appropriate section
        $SectionPattern = "## $($Entry.Category -replace 's$', 's')"
        if ($IndexContent -match $SectionPattern) {
            # Insert after section header
            $IndexContent = $IndexContent -replace "($SectionPattern`n)", "`$1$IndexLine"
            $Stats.IndexUpdates++
        } else {
            # Add to end of file
            $IndexContent += "`n## 2-atoms/$($Entry.Category)`n$IndexLine"
            $Stats.IndexUpdates++
        }
    }

    if (!$DryRun) {
        Set-Content -Path $IndexPath -Value $IndexContent -Encoding UTF8
        Write-Host "  Updated: index.md with $($Stats.IndexUpdates) entries" -ForegroundColor Green
    } else {
        Write-Host "  [DRY RUN] Would update: index.md" -ForegroundColor Yellow
    }
}

# Orphan detection
Write-Host "`nDetecting orphans..." -ForegroundColor Magenta

$Orphans = @()
$AllAtoms = Get-ChildItem -Path "$VaultPath\2-atoms" -Filter "*.md" -Recurse

foreach ($Atom in $AllAtoms) {
    $Age = (Get-Date) - $Atom.CreationTime
    if ($Age.TotalDays -lt 7) { continue }  # Skip recent atoms

    $Concept = [System.IO.Path]::GetFileNameWithoutExtension($Atom.Name)

    # Check for incoming links
    $HasBacklinks = $false
    foreach ($OtherFile in $AllAtoms) {
        if ($OtherFile.FullName -eq $Atom.FullName) { continue }
        try {
            $OtherContent = Get-Content $OtherFile.FullName -Raw
            if ($OtherContent -match "\[\[$Concept\]\]") {
                $HasBacklinks = $true
                break
            }
        } catch { continue }
    }

    if (!$HasBacklinks) {
        $Orphans += @{
            Path = $Atom.FullName
            Concept = $Concept
            Created = $Atom.CreationTime.ToString("yyyy-MM-dd")
        }
        $Stats.OrphansFound++
    }
}

if ($Orphans.Count -gt 0) {
    $OrphanReportPath = "$VaultPath\3-threads\orphans\$((Get-Date).ToString('yyyy-MM')) — Orphan Report.md"

    if (!(Test-Path (Split-Path $OrphanReportPath))) {
        New-Item -ItemType Directory -Path (Split-Path $OrphanReportPath) -Force | Out-Null
    }

    $OrphanContent = @"
## Orphan Report — $((Get-Date).ToString('yyyy-MM'))

**Notes with 0 incoming links (7+ days old):**

"@

    foreach ($Orphan in $Orphans) {
        $OrphanContent += @"
1. [[$($Orphan.Concept)]] — created $($Orphan.Created)
   - Suggested links: Check related concepts in same category
   - Action: [ ] Add to index, [ ] Link from related notes

"@
    }

    if (!$DryRun) {
        Set-Content -Path $OrphanReportPath -Value $OrphanContent -Encoding UTF8
        Write-Host "  Created orphan report: $OrphanReportPath" -ForegroundColor Gray
    }
}

# Update log.md
Write-Host "`nUpdating log.md..." -ForegroundColor Magenta
$LogEntry = @"

## [$Timestamp] Editor Run | Linked $($Stats.AtomsProcessed) atoms, flagged $($Stats.FrictionFlags) conflicts
- New atoms processed: $($Stats.AtomsProcessed)
- Links added: $($Stats.OutgoingLinks + $Stats.IncomingLinks) (outgoing: $($Stats.OutgoingLinks), incoming: $($Stats.IncomingLinks))
- [FRICTION] blocks created: $($Stats.FrictionFlags)
- Index updated: $($Stats.IndexUpdates) new entries
- Orphan check: $($Stats.OrphansFound) notes with 0 incoming links (see 3-threads/orphans/)
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

## Editor Run Summary — $Timestamp

**Linking:**
- Processed: $($Stats.AtomsProcessed) new atoms
- Outgoing links added: $($Stats.OutgoingLinks)
- Incoming backlinks created: $($Stats.IncomingLinks)

**Index Updates:**
- New index entries: $($Stats.IndexUpdates)

**[FRICTION] Flags (needs your review):**
"@

if ($FrictionBlocks.Count -gt 0) {
    foreach ($Flag in $FrictionBlocks) {
        $BriefSection += "`n1. `3-threads/_friction\$($Flag.File)` — $($Flag.Description)"
    }
} else {
    $BriefSection += "`nNone detected"
}

$BriefSection += @"

**Orphan Watch:**
- Current orphans (7+ days, 0 links): $($Stats.OrphansFound) notes
- Full report: `3-threads/orphans/$((Get-Date).ToString('yyyy-MM')) — Orphan Report.md`

**Action Needed:**
- [ ] Resolve [FRICTION] conflicts (priority: high)
- [ ] Skim 2-3 new atoms to verify linking quality
- [ ] Check orphan report for false positives

---
*Editor Run section — $Timestamp*
"@

if (!$DryRun) {
    if (Test-Path $BriefPath) {
        Add-Content -Path $BriefPath -Value $BriefSection -Encoding UTF8
    } else {
        $FullBrief = @"
---
date: $Date
type: daily-briefing
tags: [morning-brief, editor-output]
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
Write-Host "`n=== Editor Run Complete ===" -ForegroundColor Cyan
Write-Host "Atoms Processed: $($Stats.AtomsProcessed)" -ForegroundColor White
Write-Host "Links Added: $($Stats.OutgoingLinks + $Stats.IncomingLinks)" -ForegroundColor Gray
Write-Host "Friction Flags: $($Stats.FrictionFlags)" -ForegroundColor $(if ($Stats.FrictionFlags -gt 0) { "Red" } else { "Gray" })
Write-Host "Duration: $([Math]::Round((Get-Date - $StartTime).TotalSeconds, 1)) seconds" -ForegroundColor Gray