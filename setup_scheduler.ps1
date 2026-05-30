$action = New-ScheduledTaskAction -Execute "python" -Argument "E:\ObsidianVault\morning_digest.py"
$trigger = New-ScheduledTaskTrigger -Daily -At 7:30AM
Register-ScheduledTask -TaskName "ObsidianMorningDigest" -Action $action -Trigger $trigger -RunLevel Highest