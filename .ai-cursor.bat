@echo off
@REM ===========================================================================
@REM File:         .ai-cursor.bat
@REM Description:
@REM   Launcher for Cursor IDE. Installs via winget if missing, and cleanly
@REM   detaches the console window by directly launching the .exe.
@REM
@REM Usage:
@REM   Double-click to open the current directory in Cursor, or pass a path
@REM   as an argument.
@REM
@REM Requirements:
@REM   - winget (App Installer)
@REM
@REM Date:
@REM   2026-06-16
@REM Version:
@REM   1.2
@REM ===========================================================================

set "GREEN=[32m"
set "YELLOW=[33m"
set "CYAN=[36m"
set "RESET=[0m"

echo.%CYAN%Checking for Cursor IDE...%RESET%
where cursor >nul 2>&1 || (
    echo.%YELLOW%Cursor not found. Installing via winget...%RESET%
    winget install --id "Anysphere.Cursor" --exact --accept-package-agreements --accept-source-agreements --force
)

set "TARGET=%~1"
if "%TARGET%"=="" set "TARGET=%~dp0."

set "LAUNCH_ARGS="%TARGET%""
if exist "%USERPROFILE%\.bashrc" set "LAUNCH_ARGS=%LAUNCH_ARGS% "%USERPROFILE%\.bashrc""
if exist "%TARGET%\README.md" set "LAUNCH_ARGS=%LAUNCH_ARGS% "%TARGET%\README.md""

echo.%GREEN%Launching Cursor...%RESET%

@REM We must launch the raw .exe directly. 
@REM Using the global 'cursor' command invokes a .cmd wrapper, which forces the console window to remain open.
set "EXE=%LOCALAPPDATA%\Programs\cursor\Cursor.exe"
if not exist "%EXE%" set "EXE=%LOCALAPPDATA%\Programs\Cursor\Cursor.exe"

if exist "%EXE%" (
    start "" "%EXE%" %LAUNCH_ARGS%
) else (
    start /b "" cursor %LAUNCH_ARGS%
)

exit