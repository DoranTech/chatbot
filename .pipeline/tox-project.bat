set PATH=%PYTHON310%;%PYTHON311%

call venv\Scripts\activate.bat

tox -r -e %1

if %ERRORLEVEL% NEQ 0 (
    exit /B 1
)