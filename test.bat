@echo off
REM Test system
cd /d "%~dp0"
set PYTHON_PATH=C:/Users/kane.nguyen/AppData/Local/Programs/Python/Python313/python.exe
echo 🧪 Chạy full test system...
"%PYTHON_PATH%" main.py
echo.
echo ✅ Test hoàn tất!
pause
