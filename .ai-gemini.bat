@echo off
@REM ===========================================================================
@REM File:         .ai-gemini.bat
@REM Description:
@REM   This script ensures the Google Gemini CLI is installed and updated,
@REM   then launches an interactive session.
@REM
@REM Usage:
@REM   Double-click to start your Gemini session. You will be given a brief
@REM   prompt to optionally update the CLI before the session begins, saving
@REM   startup time if you just want to jump straight in.
@REM
@REM Requirements:
@REM   - Node.js (and npm) must be installed and in the system PATH.
@REM
@REM Date:
@REM   2026-06-16
@REM Version:
@REM   1.1
@REM ===========================================================================

@REM --- Hard-coded ANSI/VT color variables ---
set "RED=[31m"
set "GREEN=[32m"
set "YELLOW=[33m"
set "CYAN=[36m"
set "RESET=[0m"

goto :main

@REM ---------------------------------------------------------------------------
@REM Function: Check-Node
@REM Purpose: Ensures Node.js and npm are available.
@REM ---------------------------------------------------------------------------
:Check-Node
node --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.%RED%Error: Node.js is not recognized.%RESET%
    echo.%YELLOW%Please ensure Node.js is installed and added to your PATH.%RESET%
    pause
    exit /b 1
)
goto :EOF

@REM ---------------------------------------------------------------------------
@REM Function: Check-And-Update-Gemini
@REM Purpose: Checks if Gemini CLI is installed. If not, installs it.
@REM          If it is, gives the user a 2-second choice to update it.
@REM ---------------------------------------------------------------------------
:Check-And-Update-Gemini
echo.%CYAN%=========================================================%RESET%
echo.Checking %YELLOW%Gemini CLI%RESET% status...

call gemini --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.%YELLOW%Gemini CLI not found. Installing the latest version globally...%RESET%
    call npm install -g @google/gemini-cli@latest
    if %ERRORLEVEL% NEQ 0 (
        echo.%RED%Failed to install Gemini CLI. Check your internet connection.%RESET%
        pause
        exit /b 1
    )
    echo.%GREEN%Installation complete.%RESET%
    goto :EOF
)

echo.%GREEN%Gemini CLI is installed.%RESET%
echo.
@REM Ask user if they want to update.
echo.%CYAN%Do you want to check for and install updates?%RESET%
choice /C YN /M "Press Y for Yes, N for No"
if errorlevel 2 goto :skip_update
if errorlevel 1 (
    echo.
    echo.%YELLOW%Updating Gemini CLI to the latest version...%RESET%
    call npm install -g @google/gemini-cli@latest
)
:skip_update
echo.
goto :EOF

@REM ---------------------------------------------------------------------------
@REM Function: Start-Gemini
@REM Purpose: Launches the interactive Gemini CLI session.
@REM ---------------------------------------------------------------------------
:Start-Gemini
echo.%CYAN%=========================================================%RESET%
echo.%GREEN%Starting Gemini CLI Interactive Session...%RESET%
echo.

@REM Set your preferred model here. 
set "MODEL=gemini-3-flash-preview"

@REM Launch the CLI
call gemini --model %MODEL%

goto :EOF

@REM ---------------------------------------------------------------------------
@REM Function: Check-Execution-Policy
@REM Purpose: Ensures PowerShell execution policy allows running scripts.
@REM ---------------------------------------------------------------------------
:Check-Execution-Policy
powershell -NoProfile -Command "$policy = Get-ExecutionPolicy; if ($policy -eq 'Restricted') { exit 1 } else { exit 0 }" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.%RED%Error: PowerShell script execution is restricted.%RESET%
    echo.%YELLOW%This prevents Gemini CLI and Node.js tools from running properly.%RESET%
    echo.
    echo.Please open a regular PowerShell window and run the following command:
    echo.%CYAN%Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser%RESET%
    echo.
    pause
    exit /b 1
)
goto :EOF

@REM ===========================================================================
:main
@REM Main execution starts here
@REM ===========================================================================
call :Check-Execution-Policy
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

call :Check-Node
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

call :Check-And-Update-Gemini
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

call :Start-Gemini

echo.
echo.%CYAN%=========================================================%RESET%
echo.%YELLOW%Session ended.%RESET%
pause
exit /b 0