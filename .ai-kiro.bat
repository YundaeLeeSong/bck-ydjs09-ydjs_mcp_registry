@echo off
@REM ===========================================================================
@REM File:         .ai-kiro.bat
@REM Description:
@REM   Launcher for Kiro IDE. Installs via winget if missing, and cleanly
@REM   detaches the console window by directly launching the .exe.
@REM
@REM Usage:
@REM   Double-click to open the current directory in Kiro, or pass a path
@REM   as an argument.
@REM
@REM Requirements:
@REM   - winget (App Installer)
@REM
@REM Date:
@REM   2026-06-16
@REM Version:
@REM   1.1
@REM ===========================================================================

set "GREEN=[32m"
set "YELLOW=[33m"
set "CYAN=[36m"
set "RESET=[0m"

echo.%CYAN%Checking for Kiro IDE...%RESET%
where kiro >nul 2>&1 || (
    echo.%YELLOW%Kiro not found. Installing via winget...%RESET%
    winget install --id "Amazon.Kiro" --exact --accept-package-agreements --accept-source-agreements --force
)

set "TARGET=%~1"
if "%TARGET%"=="" set "TARGET=%~dp0."

echo.%GREEN%Launching Kiro...%RESET%

@REM We must launch the raw .exe directly. 
@REM Using the global 'kiro' command invokes a .cmd wrapper, which forces the console window to remain open.
set "EXE=%LOCALAPPDATA%\Programs\kiro\Kiro.exe"
if not exist "%EXE%" set "EXE=%LOCALAPPDATA%\Programs\Kiro\Kiro.exe"

if exist "%EXE%" (
    start "" "%EXE%" "%TARGET%"
) else (
    start /b "" kiro "%TARGET%"
)

exit