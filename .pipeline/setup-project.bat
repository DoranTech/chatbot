%BASE_PYTHON% -m venv venv
CALL venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install tox

if %ERRORLEVEL% NEQ 0 (
    exit /B 1
)