@echo off
rem Windows launcher: finds a Python interpreter and hands over to start.py,
rem which checks the virtual environment, installs what is missing and starts
rem the simulation or the computer.   Try:  start.bat help
setlocal
cd /d "%~dp0"

if defined PYTHON (
    "%PYTHON%" start.py %*
    goto :done
)

where py >nul 2>&1
if %errorlevel% equ 0 (
    py -3 start.py %*
    goto :done
)

where python >nul 2>&1
if %errorlevel% equ 0 (
    python start.py %*
    goto :done
)

echo [start] error: no Python interpreter found on the PATH. 1>&2
echo         Install Python 3.10 or newer from https://www.python.org and tick 1>&2
echo         "Add python.exe to PATH" in the installer (or install the "py" launcher). 1>&2
exit /b 1

:done
exit /b %errorlevel%
