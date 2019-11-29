@echo off
python --version 2>NUL
if errorlevel 1 goto errorNoPython
echo Installing python modules
pip install --quiet -r requirements.txt
if errorlevel 1 goto errorNoRequirements
py -m manic_messenger
pause
goto eof

:errorNoPython
echo.
echo Error^: Python not installed. Please visit https://www.python.org/downloads/ and download the latest version of Python 3
pause
goto eof

:errorNoRequirements
echo.
echo Error^: requirements.txt not found
pause
goto eof