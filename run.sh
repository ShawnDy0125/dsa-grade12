#!/bin/bash
# DSA Grade 12 - Run Script for Unix/Linux/MacOS
# Cách sử dụng: ./run.sh [problem]
# Ví dụ: ./run.sh palindrome
#       ./run.sh fibonacci  
#       ./run.sh triangles
#       ./run.sh (chạy tất cả)

cd "$(dirname "$0")"

if [ -z "$1" ]; then
    echo "🚀 Chạy tất cả test cases..."
    python main.py
else
    echo "🚀 Chạy test cho bài: $1"
    python main.py --problem "$1"
fi

echo ""
echo "✅ Hoàn thành!"
