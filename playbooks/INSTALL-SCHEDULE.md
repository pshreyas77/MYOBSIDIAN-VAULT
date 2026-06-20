# Night Shift — Manual Installation Guide

## Option 1: Run as Administrator (Recommended)

1. **Open PowerShell as Administrator**
   - Right-click PowerShell → "Run as Administrator"

2. **Execute the setup script**
   ```powershell
   cd "E:\_Knowledge\ObsidianVault\playbooks"
   .\setup-night-shift.ps1
   ```

3. **Verify installation**
   ```powershell
   Get-ScheduledTask "Ruflo Night Shift*"
   ```

## Option 2: Manual Task Creation (GUI)

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create Basic Task: Scout Run**
   - Action → Create Basic Task...
   - Name: `Ruflo Night Shift - Scout Run`
   - Trigger: Daily
   - Start: 11:00 PM
   - Action: Start a program
   - Program: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`
   - Arguments: `-NoProfile -ExecutionPolicy Bypass -File "E:\_Knowledge\ObsidianVault\playbooks\scout-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"`
   - Start in: `E:\_Knowledge\ObsidianVault\playbooks`
   - Check "Open properties..." before Finish

3. **Configure Properties**
   - General tab:
     - ☑ Run with highest privileges
     - Configure for: Windows 11
   - Conditions tab:
     - ☑ Start the task only if on AC power (optional)
   - Settings tab:
     - ☑ Allow task to be run on demand
     - ☑ Run task as soon as possible after scheduled start is missed

4. **Repeat for Refinery Run (3:00 AM)**
   - Same steps, different time and script:
   - Arguments: `-NoProfile -ExecutionPolicy Bypass -File "E:\_Knowledge\ObsidianVault\playbooks\refinery-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"`

5. **Repeat for Editor Run (6:00 AM)**
   - Same steps, different time and script:
   - Arguments: `-NoProfile -ExecutionPolicy Bypass -File "E:\_Knowledge\ObsidianVault\playbooks\editor-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"`

## Option 3: Use .bat File Triggers

Create batch files that can be double-clicked or added to startup:

### Scout Run Trigger
Create `E:\_Knowledge\ObsidianVault\playbooks\trigger-scout.bat`:
```batch
@echo off
echo [Scout Run - %DATE% %TIME%]
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scout-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"
pause
```

### Refinery Run Trigger
Create `E:\_Knowledge\ObsidianVault\playbooks\trigger-refinery.bat`:
```batch
@echo off
echo [Refinery Run - %DATE% %TIME%]
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0refinery-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"
pause
```

### Editor Run Trigger
Create `E:\_Knowledge\ObsidianVault\playbooks\trigger-editor.bat`:
```batch
@echo off
echo [Editor Run - %DATE% %TIME%]
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0editor-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"
pause
```

## Option 4: WSL/Linux Cron Jobs

If using WSL, add to crontab:

```bash
# Edit crontab
crontab -e

# Add Night Shift schedule (adjust path for WSL mount point)
0 23 * * * /mnt/c/Windows/System32/powershell.exe -NoProfile -ExecutionPolicy Bypass -File /mnt/e/_Knowledge/ObsidianVault/playbooks/scout-run.ps1 -VaultPath /mnt/e/_Knowledge/ObsidianVault
0 3 * * * /mnt/c/Windows/System32/powershell.exe -NoProfile -ExecutionPolicy Bypass -File /mnt/e/_Knowledge/ObsidianVault/playbooks/refinery-run.ps1 -VaultPath /mnt/e/_Knowledge/ObsidianVault
0 6 * * * /mnt/c/Windows/System32/powershell.exe -NoProfile -ExecutionPolicy Bypass -File /mnt/e/_Knowledge/ObsidianVault/playbooks/editor-run.ps1 -VaultPath /mnt/e/_Knowledge/ObsidianVault
```

## Verification

After installation, verify:

```powershell
# Check all Night Shift tasks
Get-ScheduledTask "Ruflo Night Shift*" | Format-Table TaskName, State, LastRunTime, NextRunTime

# Check individual task details
Get-ScheduledTaskInfo "Ruflo Night Shift - Scout Run"

# Run manually for testing
Start-ScheduledTask "Ruflo Night Shift - Scout Run"
Start-Sleep -Seconds 5
Get-ScheduledTaskInfo "Ruflo Night Shift - Scout Run" | Select-Object LastRunTime, LastTaskResult
```

## Troubleshooting Access Denied

If you get "Access is denied":

1. **Run PowerShell as Administrator**
   - Right-click PowerShell → Run as Administrator
   - Then execute the setup script

2. **Check User Account Control (UAC)**
   - You may need to approve the UAC prompt

3. **Alternative: Use GUI**
   - Task Scheduler GUI handles elevation automatically

## First Test Run

Before relying on automation, test each script manually:

```powershell
cd "E:\_Knowledge\ObsidianVault\playbooks"

# Test Scout (dry run first)
.\scout-run.ps1 -DryRun -VaultPath "E:\_Knowledge\ObsidianVault"

# Then actual run
.\scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"

# Check output files
Get-ChildItem "..\1-desk\*.md" | Select-Object Name, LastWriteTime
Get-ChildItem "..\briefings\*.md" | Select-Object Name, LastWriteTime
```

---

**Support:** See `NIGHT-SHIFT-RUNBOOK.md` for full documentation.