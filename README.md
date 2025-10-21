# DSA Practice - Grade 12

## 📖 Mô tả
Repository này chứa các bài tập Data Structures & Algorithms (DSA) dành cho học sinh lớp 12. Mỗi bài đều có:
- Đề bài chi tiết với ví dụ
- Giải thích thuật toán  
- Test cases đầy đủ
- Cách chạy và kiểm tra kết quả

## 🚀 Cách sử dụng

### 1. Chạy bằng script đơn giản (RECOMMENDED) 🚀
```cmd
# Chạy tất cả test cases
.\run.bat

# Chạy test riêng từng bài
.\run.bat palindrome
.\run.bat fibonacci
.\run.bat triangles
.\run.bat triangle-right
.\run.bat triangle-isosceles  
.\run.bat triangle-hollow

# Demo với giải thích chi tiết
.\demo palindrome
.\demo fibonacci

```

### 2. Chạy trực tiếp bằng Python
```bash
# Chạy tất cả test cases
python main.py

# Chạy test cho bài cụ thể
python main.py --problem fibonacci
python main.py --problem triangles

# Chạy từng file riêng lẻ
python problems/palindrome.py
python problems/fibonacci.py
```

## 📁 Cấu trúc project

```
dsa-grade12/
├── main.py                    # File chính để chạy test
├── problems/                  # Thư mục chứa các bài tập
│   ├── __init__.py
│   ├── palindrome.py         # Bài 1: Kiểm tra Palindrome
│   ├── fibonacci.py          # Bài 2: Kiểm tra Fibonacci
│   ├── triangle_right.py     # Bài 3: Tam giác vuông
│   ├── triangle_isosceles.py # Bài 4: Tam giác cân  
│   └── triangle_hollow.py    # Bài 5: Tam giác rỗng
├── run.bat                    # 🚀 Script chạy chính (Windows)
├── run.sh                     # 🚀 Script chạy chính (Unix/Linux)  
├── run.ps1                    # 🚀 Script chạy chính (PowerShell)
├── demo.bat                   # 🧪 Demo từng bài riêng
├── test.bat                   # ✅ Test full hệ thống
├── help.bat                   # ❓ Hướng dẫn commands
└── README.md                  # Hướng dẫn sử dụng
```

## 📝 Danh sách bài tập

### Bài 1: Is Palindrome
- **File**: `problems/palindrome.py`
- **Mô tả**: Kiểm tra số có phải palindrome không
- **Ví dụ**: 121 → True, -121 → False
- **Test**: `python main.py --problem palindrome`

### Bài 2: Is Fibonacci  
- **File**: `problems/fibonacci.py`
- **Mô tả**: Kiểm tra số có trong dãy Fibonacci không
- **Ví dụ**: 13 → True, 14 → False
- **Test**: `python main.py --problem fibonacci`

### Bài 3: Right Triangle
- **File**: `problems/triangle_right.py`
- **Mô tả**: Vẽ tam giác sao vuông (góc vuông bên trái)
- **Ví dụ**: n=3 → `["*", "**", "***"]`
- **Test**: `python main.py --problem triangle-right`

### Bài 4: Isosceles Triangle
- **File**: `problems/triangle_isosceles.py`  
- **Mô tả**: Vẽ tam giác sao cân (đỉnh ở trên)
- **Ví dụ**: n=3 → `["  *", " ***", "*****"]`
- **Test**: `python main.py --problem triangle-isosceles`

### Bài 5: Hollow Triangle
- **File**: `problems/triangle_hollow.py`
- **Mô tả**: Vẽ tam giác sao rỗng (chỉ có viền)
- **Ví dụ**: n=3 → `["  *", " * *", "*****"]`
- **Test**: `python main.py --problem triangle-hollow`

## 💡 Hướng dẫn cho học sinh

### Bước 1: Pull code về
```bash
git pull origin main
```

### Bước 2: Đọc đề bài
Mở file trong thư mục `problems/` để đọc đề bài và yêu cầu

### Bước 3: Code thuật toán
Tìm phần `# TODO: Em hãy implement thuật toán ở đây` và viết code

### Bước 4: Test code
Chạy test để kiểm tra kết quả:
```bash
python main.py --problem [tên_bài]
```

### Bước 5: Giải thích thuật toán
Thêm comment giải thích logic và độ phức tạp

## ✅ Ví dụ output khi chạy test

```
🚀 DSA PRACTICE - GRADE 12
==================================================
TESTING: Is Palindrome
==================================================
Test 1: Số đối xứng
  Input: 121
  Expected: True, Got: True
  Status: ✅ PASS

Test 2: Số âm không phải palindrome
  Input: -121
  Expected: False, Got: False
  Status: ✅ PASS

Results: 7/7 tests passed
==================================================
🎉 TẤT CẢ TEST ĐỀU PASS!
==================================================
```

## 🎯 Tips cho học sinh

1. **Đọc kỹ đề bài** - Hiểu rõ input/output và constraints
2. **Phân tích test cases** - Hiểu các trường hợp edge case
3. **Code từng bước** - Implement logic từ đơn giản đến phức tạp
4. **Test thường xuyên** - Chạy test sau mỗi thay đổi
5. **Optimize sau** - Làm đúng trước, optimize sau

## 📚 Kiến thức cần có

- Python cơ bản (variables, functions, loops, conditions)
- String manipulation và slicing
- Basic math operations
- Time & Space Complexity analysis

---

**Happy Coding! 🎉**
