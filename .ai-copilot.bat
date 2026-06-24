@echo off
@REM ===========================================================================
@REM File:         .ai-copilot.bat
@REM Description:
@REM   Launcher for Visual Studio Code (GitHub Copilot compatible). Installs
@REM   via winget if missing, and cleanly detaches the console window by
@REM   directly launching Code.exe.
@REM
@REM Usage:
@REM   Double-click to open the current directory in VS Code, or pass a path
@REM   as an argument. Also opens .bashrc and README.md when they exist.
@REM
@REM Requirements:
@REM   - winget (App Installer)
@REM
@REM Date:
@REM   2026-06-19
@REM Version:
@REM   1.2
@REM ===========================================================================

set "GREEN=[32m"
set "YELLOW=[33m"
set "CYAN=[36m"
set "RESET=[0m"

echo.%CYAN%Checking for Visual Studio Code...%RESET%
where code >nul 2>&1 || (
    echo.%YELLOW%VS Code not found. Installing via winget...%RESET%
    winget install --id "Microsoft.VisualStudioCode" --exact --accept-package-agreements --accept-source-agreements --force
)

set "TARGET=%~1"
if "%TARGET%"=="" set "TARGET=%~dp0."

set "LAUNCH_ARGS="%TARGET%""
if exist "%USERPROFILE%\.bashrc" set "LAUNCH_ARGS=%LAUNCH_ARGS% "%USERPROFILE%\.bashrc""
if exist "%TARGET%\README.md" set "LAUNCH_ARGS=%LAUNCH_ARGS% "%TARGET%\README.md""

echo.%GREEN%Launching VS Code...%RESET%

@REM We must launch the raw .exe directly.
@REM Using the global 'code' command invokes a .cmd wrapper, which forces the console window to remain open.
set "EXE=%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
if not exist "%EXE%" set "EXE=%ProgramFiles%\Microsoft VS Code\Code.exe"

if exist "%EXE%" (
    start "" "%EXE%" %LAUNCH_ARGS%
) else (
    start /b "" code %LAUNCH_ARGS%
)

exit
