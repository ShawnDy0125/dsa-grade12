"""
DSA Practice - Grade 12
Main runner để test các bài tập DSA

Cách chạy:
- Chạy tất cả test: python main.py
- Chạy test cụ thể: python main.py --problem palindrome
"""

import sys
import argparse
from problems.palindrome import Solution as PalindromeSolution
from problems.fibonacci import Solution as FibonacciSolution
from problems.triangle_right import Solution as TriangleRightSolution
from problems.triangle_isosceles import Solution as TriangleIsoscelesSolution
from problems.triangle_hollow import Solution as TriangleHollowSolution


def test_palindrome():
    """Test bài Palindrome"""
    print("=" * 50)
    print("TESTING: Is Palindrome")
    print("=" * 50)
    
    solution = PalindromeSolution()
    
    # Test cases
    test_cases = [
        (121, True, "Số đối xứng"),
        (-121, False, "Số âm không phải palindrome"),
        (10, False, "Số có 0 ở cuối"),
        (0, True, "Số 0"),
        (1221, True, "Số chẵn đối xứng"),
        (12321, True, "Số lẻ đối xứng"),
        (123, False, "Số không đối xứng")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_val, expected, description) in enumerate(test_cases, 1):
        result = solution.isPalindrome(input_val)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: {input_val}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    return passed == total


def test_fibonacci():
    """Test bài Fibonacci"""
    print("=" * 50)
    print("TESTING: Is Fibonacci Number")
    print("=" * 50)
    
    solution = FibonacciSolution()
    
    # Test cases
    test_cases = [
        (0, True, "Fibonacci đầu tiên"),
        (1, True, "Fibonacci thứ 2 và 3"),
        (2, True, "Fibonacci thứ 4"),
        (3, True, "Fibonacci thứ 5"),
        (5, True, "Fibonacci thứ 6"),
        (8, True, "Fibonacci thứ 7"),
        (13, True, "Fibonacci thứ 8"),
        (4, False, "Không phải Fibonacci"),
        (6, False, "Không phải Fibonacci"),
        (7, False, "Không phải Fibonacci"),
        (21, True, "Fibonacci lớn hơn"),
        (22, False, "Không phải Fibonacci lớn")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_val, expected, description) in enumerate(test_cases, 1):
        result = solution.isFibonacci(input_val)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: {input_val}")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    return passed == total


def test_triangle_right():
    """Test bài Right Triangle"""
    print("=" * 50)
    print("TESTING: Right Triangle Pattern")
    print("=" * 50)
    
    solution = TriangleRightSolution()
    
    # Test cases
    test_cases = [
        (1, ["*"], "Tam giác 1 dòng"),
        (2, ["*", "**"], "Tam giác 2 dòng"),
        (3, ["*", "**", "***"], "Tam giác 3 dòng"),
        (4, ["*", "**", "***", "****"], "Tam giác 4 dòng"),
        (5, ["*", "**", "***", "****", "*****"], "Tam giác 5 dòng"),
        (0, [], "Edge case: n=0")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_val, expected, description) in enumerate(test_cases, 1):
        result = solution.printRightTriangle(input_val)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: n={input_val}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    return passed == total


def test_triangle_isosceles():
    """Test bài Isosceles Triangle"""
    print("=" * 50)
    print("TESTING: Isosceles Triangle Pattern")
    print("=" * 50)
    
    solution = TriangleIsoscelesSolution()
    
    # Test cases
    test_cases = [
        (1, ["*"], "Tam giác cân 1 dòng"),
        (2, [" *", "***"], "Tam giác cân 2 dòng"),
        (3, ["  *", " ***", "*****"], "Tam giác cân 3 dòng"),
        (4, ["   *", "  ***", " *****", "*******"], "Tam giác cân 4 dòng"),
        (0, [], "Edge case: n=0")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_val, expected, description) in enumerate(test_cases, 1):
        result = solution.printIsoscelesTriangle(input_val)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: n={input_val}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    return passed == total


def test_triangle_hollow():
    """Test bài Hollow Triangle"""
    print("=" * 50)
    print("TESTING: Hollow Triangle Pattern")
    print("=" * 50)
    
    solution = TriangleHollowSolution()
    
    # Test cases
    test_cases = [
        (1, ["*"], "Tam giác rỗng 1 dòng"),
        (2, [" *", "***"], "Tam giác rỗng 2 dòng"),
        (3, ["  *", " * *", "*****"], "Tam giác rỗng 3 dòng"),
        (4, ["   *", "  * *", " *   *", "*******"], "Tam giác rỗng 4 dòng"),
        (5, ["    *", "   * *", "  *   *", " *     *", "*********"], "Tam giác rỗng 5 dòng"),
        (0, [], "Edge case: n=0")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_val, expected, description) in enumerate(test_cases, 1):
        result = solution.printHollowTriangle(input_val)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Test {i}: {description}")
        print(f"  Input: n={input_val}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print(f"  Status: {status}")
        print()
        
        if result == expected:
            passed += 1
    
    print(f"Results: {passed}/{total} tests passed")
    return passed == total


def main():
    parser = argparse.ArgumentParser(description='DSA Practice Runner')
    parser.add_argument('--problem', choices=[
        'palindrome', 'fibonacci', 'triangle-right', 'triangle-isosceles', 
        'triangle-hollow', 'triangles', 'all'
    ], default='all', help='Chọn bài để test')
    
    args = parser.parse_args()
    
    print("🚀 DSA PRACTICE - GRADE 12")
    print("=" * 50)
    
    all_passed = True
    
    if args.problem in ['palindrome', 'all']:
        try:
            if not test_palindrome():
                all_passed = False
        except Exception as e:
            print(f"❌ Error testing Palindrome: {e}")
            all_passed = False
    
    if args.problem in ['fibonacci', 'all']:
        try:
            if not test_fibonacci():
                all_passed = False
        except Exception as e:
            print(f"❌ Error testing Fibonacci: {e}")
            all_passed = False
    
    if args.problem in ['triangle-right', 'triangles', 'all']:
        try:
            if not test_triangle_right():
                all_passed = False
        except Exception as e:
            print(f"❌ Error testing Right Triangle: {e}")
            all_passed = False
    
    if args.problem in ['triangle-isosceles', 'triangles', 'all']:
        try:
            if not test_triangle_isosceles():
                all_passed = False
        except Exception as e:
            print(f"❌ Error testing Isosceles Triangle: {e}")
            all_passed = False
    
    if args.problem in ['triangle-hollow', 'triangles', 'all']:
        try:
            if not test_triangle_hollow():
                all_passed = False
        except Exception as e:
            print(f"❌ Error testing Hollow Triangle: {e}")
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 TẤT CẢ TEST ĐỀU PASS!")
    else:
        print("😞 MỘT SỐ TEST CHƯA PASS - HẢY KIỂM TRA LẠI CODE")
    print("=" * 50)


if __name__ == "__main__":
    main()
