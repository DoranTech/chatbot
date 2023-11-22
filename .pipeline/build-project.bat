rmdir /S /Q build
rmdir /S /Q dist

python -m build --no-isolation
pyinstaller --name "chatbot" "chatb\__main__.py" --paths venv/Lib/site-packages --onefile
rem pyinstaller chatbot.spec

if %ERRORLEVEL% NEQ 0 (
    exit /B 1
)