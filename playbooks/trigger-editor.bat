@echo off
REM Editor Run Trigger — Double-click to run manually
echo ================================================
echo [Editor Run — %DATE% %TIME%]
echo ================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0editor-run.ps1" -VaultPath "E:\_Knowledge\ObsidianVault"

echo.
echo ================================================
echo [Complete — Check index.md and _friction\ folder]
echo ================================================
pause