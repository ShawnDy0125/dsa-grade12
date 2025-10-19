@echo off
REM Demo individual problems

if "%1"=="" (
    echo ❌ Cần chỉ định bài để demo
    echo Ví dụ: demo palindrome
    echo        demo fibonacci
    pause
    exit /b 1
)

cd /d "%~dp0"

set PYTHON_PATH=C:/Users/kane.nguyen/AppData/Local/Programs/Python/Python313/python.exe

if "%1"=="palindrome" (
    echo 🧪 Demo Palindrome...
    "%PYTHON_PATH%" problems/palindrome.py
) else if "%1"=="fibonacci" (
    echo 🧪 Demo Fibonacci...
    "%PYTHON_PATH%" problems/fibonacci.py
) else (
    echo ❌ Bài không tồn tại: %1
    echo Các bài có sẵn: palindrome, fibonacci
)

echo.
pause
