# DSA Grade 12 - PowerShell Run Script
# Cách sử dụng: .\run.ps1 [problem]
# Ví dụ: .\run.ps1 palindrome
#       .\run.ps1 fibonacci  
#       .\run.ps1 triangles
#       .\run.ps1 (chạy tất cả)

param(
    [string]$Problem = ""
)

Set-Location $PSScriptRoot

if ([string]::IsNullOrEmpty($Problem)) {
    Write-Host "🚀 Chạy tất cả test cases..." -ForegroundColor Green
    python main.py
} else {
    Write-Host "🚀 Chạy test cho bài: $Problem" -ForegroundColor Green  
    python main.py --problem $Problem
}

Write-Host ""
Write-Host "✅ Hoàn thành!" -ForegroundColor Cyan
Read-Host "Nhấn Enter để tiếp tục"
