rmdir /S /Q build
rmdir /S /Q dist

python -m build --no-isolation
pyinstaller chatbot.spec

if %ERRORLEVEL% NEQ 0 (
    exit /B 1
)