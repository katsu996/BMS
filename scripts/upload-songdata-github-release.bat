@echo off
setlocal
rem Stay in the folder that contains this .bat and the .ps1 (often copied next to songdata.db).
rem Do not use non-ASCII here: CMD may mis-parse and break %GITHUB_TOKEN% expansion.
cd /d "%~dp0"

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0upload-songdata-github-release.ps1" %*
exit /b %ERRORLEVEL%
