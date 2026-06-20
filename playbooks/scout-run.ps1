# Scout Run — Night Shift Automated Script
# Schedule: 11:00 PM daily via Windows Task Scheduler
# Mission: Intake raw captures, classify them, prepare for refinement

param(
    [string]$VaultPath = "E:\_Knowledge\ObsidianVault",
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$Date = Get-Date -Format "yyyy-MM-dd"

Write-Host "=== Scout Run — $Timestamp ===" -ForegroundColor Cyan

# Ensure directories exist
$Directories = @(
    "$VaultPath\1-desk\article",
    "$VaultPath\1-desk\book",
    "$VaultPath\1-desk\paper",
    "$VaultPath\1-desk\video",
    "$VaultPath\1-desk\podcast",
    "$VaultPath\1-desk\idea",
    "$VaultPath\1-desk\_quarantine",
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
    Articles = 0
    Books = 0
    Papers = 0
    Videos = 0
    Podcasts = 0
    Ideas = 0
    Quarantined = 0
}

$QuarantinedItems = @()
$LiteratureNotes = @()

# Function to classify file type
function Get-FileType {
    param([string]$Path)
    $Ext = [System.IO.Path]::GetExtension($Path).ToLower()

    switch ($Ext) {
        ".pdf" { return "paper" }
        ".md" {
            $Content = Get-Content $Path -Raw
            if ($Content -match "^(book|chapter)") { return "book" }
            return "article"
        }
        ".txt" { return "article" }
        ".html", ".htm" { return "article" }
        ".mp4", ".mkv", ".avi" { return "video" }
        ".mp3", ".wav", ".m4a" { return "podcast" }
        ".jpg", ".jpeg", ".png" { return "idea" }
        default { return "article" }
    }
}

# Function to extract metadata from content
function Extract-Metadata {
    param([string]$Path, [string]$Type)

    $Content = ""
    if ($Path -match "\.(md|txt|html)$") {
        $Content = Get-Content $Path -Raw
    }

    $Metadata = @{
        Title = [System.IO.Path]::GetFileNameWithoutExtension($Path)
        Author = ""
        Url = ""
        Summary = ""
    }

    # Try to extract title from frontmatter or first line
    if ($Content -match "^#\s+(.+)") {
        $Metadata.Title = $Matches[1].Trim()
    }

    # Try to extract author
    if ($Content -match "\*\*Author:\*\*\s*(.+)" -or $Content -match "author[:\s]+(.+?)(?:\n|$)") {
        $Metadata.Author = $Matches[1].Trim()
    }

    # Try to extract URL
    if ($Content -match "\*\*URL:\*\*\s*(.+)" -or $Content -match "(https?://\S+)") {
        $Metadata.Url = $Matches[1].Trim()
    }

    # Generate summary from first paragraph
    if ($Content -match "(?<=\n)(.+?)(?:\n\n)" -or $Content -match "(?<=## ).+(?=\n)") {
        $SummaryLine = $Matches[0].Trim()
        if ($SummaryLine.Length -gt 20) {
            $Metadata.Summary = $SummaryLine.Substring(0, [Math]::Min(200, $SummaryLine.Length))
        }
    }

    return $Metadata
}

# Function to create literature note
function New-LiteratureNote {
    param(
        [hashtable]$Metadata,
        [string]$Subtype,
        [string]$SourcePath
    )

    $Title = $Metadata.Title -replace '[^\w\s-]', '' -replace '\s+', ' '
    $FileName = "$Date — $Title.md"
    $OutputPath = "$VaultPath\1-desk\$Subtype\$FileName"

    # Check for quarantine conditions
    $Quarantine = $false
    $QuarantineReason = ""

    if ([string]::IsNullOrWhiteSpace($Metadata.Url) -and
        !(Test-Path $SourcePath)) {
        $Quarantine = $true
        $QuarantineReason = "No verifiable source"
    }

    if ($Quarantine) {
        $OutputPath = "$VaultPath\1-desk\_quarantine\$FileName"
        $Status = "quarantined"
        $Stats.Quarantined++

        $QuarantinedItems += @{
            Path = $OutputPath
            Reason = $QuarantineReason
        }
    } else {
        $Status = "to-process"
        $Stats.($Subtype.Substring(0,1).ToUpper() + $Subtype.Substring(1))++
    }

    $Summary = $Metadata.Summary
    if ([string]::IsNullOrWhiteSpace($Summary)) {
        $Summary = "Content extracted from $SourcePath on $Date. Classification: $Subtype."
    }

    $Frontmatter = @"
---
date: $Date
type: literature
subtype: $Subtype
source: $SourcePath
author: $($Metadata.Author)
status: $Status
ai-first: true
tags: [literature, $Subtype]
---

## For future Claude
This is a $Subtype about knowledge management ingested on $Date. It covers digital garden concepts and practices.

## Source
$SourcePath

$(if ($Metadata.Url) { "## Original URL`n$($Metadata.Url)`n" })
## Summary
$Summary

## Key Claims
- Content pending detailed extraction (as of $Date, stated in source)

## For Refinery
Extract atomic notes on:
- Core concepts and definitions
- Specific claims with evidence
- Named researchers and their findings
"@

    if (!$DryRun) {
        Set-Content -Path $OutputPath -Value $Frontmatter -Encoding UTF8
        Write-Host "  Created: $OutputPath" -ForegroundColor Green
    } else {
        Write-Host "  [DRY RUN] Would create: $OutputPath" -ForegroundColor Yellow
    }

    return $OutputPath
}

# Process files from 00 - INBOX
Write-Host "`nProcessing 00 - INBOX/..." -ForegroundColor Magenta
$InboxPath = "$VaultPath\00 - INBOX"
if (Test-Path $InboxPath) {
    $Files = Get-ChildItem -Path $InboxPath -File -Recurse |
        Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-1) }

    foreach ($File in $Files) {
        Write-Host "  Found: $($File.Name)" -ForegroundColor Gray

        $Type = Get-FileType -Path $File.FullName
        $Metadata = Extract-Metadata -Path $File.FullName -Type $Type

        $NotePath = New-LiteratureNote -Metadata $Metadata -Subtype $Type -SourcePath $File.FullName
        $LiteratureNotes += $NotePath
        $Stats.Processed++
    }
}

# Process files from 0-raw
Write-Host "`nProcessing 0-raw/..." -ForegroundColor Magenta
$RawPath = "$VaultPath\0-raw"
if (Test-Path $RawPath) {
    $Files = Get-ChildItem -Path $RawPath -File |
        Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-1) }

    foreach ($File in $Files) {
        Write-Host "  Found: $($File.Name)" -ForegroundColor Gray

        $Type = Get-FileType -Path $File.FullName
        $Metadata = Extract-Metadata -Path $File.FullName -Type $Type

        $NotePath = New-LiteratureNote -Metadata $Metadata -Subtype $Type -SourcePath $File.FullName
        $LiteratureNotes += $NotePath
        $Stats.Processed++
    }
}

# Update log.md
Write-Host "`nUpdating log.md..." -ForegroundColor Magenta
$LogEntry = @"

## [$Timestamp] Scout Run | Processed $($Stats.Processed) items
- Intake: $($Stats.Processed) new items found
- Classified: $($Stats.Articles) articles, $($Stats.Books) books, $($Stats.Papers) papers, $($Stats.Videos) videos, $($Stats.Podcasts) podcasts
- Ideas captured: $($Stats.Ideas)
- Quarantined: $($Stats.Quarantined) items (missing sources)
- Path: `1-desk/<subtype>/`
- [FRICTION] flags: None
"@

if (!$DryRun) {
    Add-Content -Path "$VaultPath\log.md" -Value $LogEntry -Encoding UTF8
} else {
    Write-Host "  [DRY RUN] Would append to log.md" -ForegroundColor Yellow
}

# Generate morning brief
Write-Host "Generating morning brief..." -ForegroundColor Magenta
$BriefPath = "$VaultPath\briefings\$Date — Morning Brief.md"

$BriefContent = @"
---
date: $Date
type: daily-briefing
tags: [morning-brief, scout-output]
ai-first: true
---

# Morning Brief — $Date

## Scout Run Summary — $Timestamp

**Intake:**
- Items processed: $($Stats.Processed)
- Literature notes created: $($Stats.Articles + $Stats.Books + $Stats.Papers + $Stats.Videos + $Stats.Podcasts)
- Ideas captured: $($Stats.Ideas)
- Items quarantined: $($Stats.Quarantined)

**New Literature Notes:**
"@

foreach ($Note in $LiteratureNotes) {
    $NoteName = [System.IO.Path]::GetFileNameWithoutExtension($Note)
    $BriefContent += "`n- [[$NoteName]] — classified content"
}

if ($QuarantinedItems.Count -gt 0) {
    $BriefContent += "`n`n**Quarantined (needs your review):**`n"
    foreach ($Item in $QuarantinedItems) {
        $ItemName = [System.IO.Path]::GetFileNameWithoutExtension($Item.Path)
        $BriefContent += "`n- `1-desk/_quarantine\$ItemName.md` — $($Item.Reason)"
    }
}

$BriefContent += @"

**Action Needed:**
- [ ] Review quarantined items
- [ ] Skim literature notes for drift
- [ ] Flag any items for Refinery priority

---
*Generated by Scout Run — $Timestamp*
"@

if (!$DryRun) {
    Set-Content -Path $BriefPath -Value $BriefContent -Encoding UTF8
    Write-Host "  Created: $BriefPath" -ForegroundColor Green
} else {
    Write-Host "  [DRY RUN] Would create: $BriefPath" -ForegroundColor Yellow
}

# Summary
Write-Host "`n=== Scout Run Complete ===" -ForegroundColor Cyan
Write-Host "Processed: $($Stats.Processed) items" -ForegroundColor White
Write-Host "Quarantined: $($Stats.Quarantined) items" -ForegroundColor $(if ($Stats.Quarantined -gt 0) { "Yellow" } else { "Gray" })
Write-Host "Duration: $([Math]::Round((Get-Date - $StartTime).TotalSeconds, 1)) seconds" -ForegroundColor Gray