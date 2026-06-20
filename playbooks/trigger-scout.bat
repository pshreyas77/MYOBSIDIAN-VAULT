@echo off
REM Scout Run Trigger — Double-click to run manually
echo ================================================
echo [Scout Run — %DATE% %TIME%]
echo ================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scout-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"

echo.
echo ================================================
echo [Complete — Check briefings\ for morning brief]
echo ================================================
pause