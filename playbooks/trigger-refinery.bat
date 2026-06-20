@echo off
REM Refinery Run Trigger — Double-click to run manually
echo ================================================
echo [Refinery Run — %DATE% %TIME%]
echo ================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0refinery-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"

echo.
echo ================================================
echo [Complete — Check 2-atoms\ for new notes]
echo ================================================
pause