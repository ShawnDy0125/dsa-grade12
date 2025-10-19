@echo off
REM DSA Grade 12 - Run Script for Windows
REM Cách sử dụng: run.bat [problem]
REM Ví dụ: run.bat palindrome
REM       run.bat fibonacci  
REM       run.bat triangles
REM       run.bat (chạy tất cả)

cd /d "%~dp0"

set PYTHON_PATH=C:/Users/kane.nguyen/AppData/Local/Programs/Python/Python313/python.exe

if "%1"=="" (
    echo 🚀 Chạy tất cả test cases...
    "%PYTHON_PATH%" main.py
) else (
    echo 🚀 Chạy test cho bài: %1
    "%PYTHON_PATH%" main.py --problem %1
)

echo.
echo ✅ Hoàn thành! 
pause
