@echo off

REM This is relative path of the current working directory
set NUKE_PATH=%~dp0

REM Printing the path
echo %NUKE_PATH%

REM This is nuke launcher path
"C:\Program Files\Nuke13.2v4\Nuke13.2.exe"

