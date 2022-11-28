@echo off

call python --version

IF ERRORLEVEL 1 (
echo Install Python!
call python-3.11.0-amd64.exe
echo Run again!
exit()
)

call python -m venv env

IF EXIST env (
    CD env
)
IF EXIST Scripts (
    CD Scripts
)

call activate.bat
call python -m ensurepip
call python -m pip install -r ..\..\requirements.txt
cls
call python ..\..\frames_extraction.py
call deactivate.bat



