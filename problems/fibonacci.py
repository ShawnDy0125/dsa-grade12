"""
Bài 2: Kiểm tra số Fibonacci
Dãy Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
Mỗi số là tổng của hai số trước đó.

Ví dụ:
- 0, 1, 2, 3, 5, 8, 13, 21 là các số Fibonacci
- 4, 6, 7, 9, 10, 11, 12 không phải số Fibonacci

Yêu cầu: Implement function isFibonacci(n) trả về True/False
"""

import math


class Solution(object):
    def isFibonacci(self, n):
        """
        Kiểm tra số n có phải số Fibonacci không
        
        Args:
            n (int): Số cần kiểm tra
            
        Returns:
            bool: True nếu là số Fibonacci, False nếu không
        
        Có 3 cách approach khác nhau - Em hãy chọn 1 cách để implement:
        
        CÁCH 1 - GENERATE SEQUENCE (Dễ hiểu nhất):
        ======================================
        - Generate dãy Fibonacci cho đến khi >= n
        - Time: O(log n) vì dãy tăng exponentially 
        - Space: O(1)
        - Thuật toán:
          1. Handle edge cases (n < 0, n == 0, n == 1)
          2. Dùng 2 biến a, b để generate: a, b = b, a + b
          3. Loop cho đến khi b >= n
          4. Return b == n
        
        CÁCH 2 - PERFECT SQUARE FORMULA (Toán học):
        ==========================================
        - Dùng công thức: n là Fibonacci ⟺ (5*n² + 4) hoặc (5*n² - 4) là số chính phương
        - Time: O(1) 
        - Space: O(1)
        - Thuật toán:
          1. Check n < 0 return False
          2. Tính A = 5*n*n + 4, B = 5*n*n - 4
          3. Check A hoặc B có phải perfect square không
          4. Perfect square: sqrt(x) == int(sqrt(x))
        
        CÁCH 3 - PRECOMPUTED SET (Cho multiple queries):
        ==============================================
        - Precompute các số Fibonacci vào set, sau đó lookup
        - Time: O(1) lookup, O(k) precompute 
        - Space: O(k) với k là số lượng Fibonacci numbers
        - Thuật toán:
          1. Tạo static set chứa Fibonacci numbers đến limit
          2. Return n in fibonacci_set
        """
        
        # TODO: Em hãy chọn 1 trong 3 cách trên để implement
        # Có thể thử cả 3 cách trong cùng function để so sánh
        
        # ============ CÁCH 1: GENERATE SEQUENCE ============
        # Uncomment code dưới để dùng cách 1:
        """
        if n < 0:
            return False
        if n == 0 or n == 1:
            return True
            
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        
        return b == n
        """
        
        # ============ CÁCH 2: PERFECT SQUARE FORMULA ============ 
        # Uncomment code dưới để dùng cách 2:
        """
        def is_perfect_square(x):
            if x < 0:
                return False
            root = int(math.sqrt(x))
            return root * root == x
        
        if n < 0:
            return False
        
        return (is_perfect_square(5 * n * n + 4) or 
                is_perfect_square(5 * n * n - 4))
        """
        
        # ============ CÁCH 3: PRECOMPUTED SET ============
        # Uncomment code dưới để dùng cách 3:
        """
        if not hasattr(self.__class__, '_fib_set'):
            self.__class__._fib_set = set()
            a, b = 0, 1
            while a <= 10**10:  # Reasonable limit
                self.__class__._fib_set.add(a)
                a, b = b, a + b
        
        return n in self.__class__._fib_set
        """
        
        # ============ DEFAULT IMPLEMENTATION ============
        # TODO: Implement ở đây
        # Viết code ở đây
class Solution(object):
  def isFibonacci(self, n):
    a, b = 0, 1
    if n == 0:
      return True
    while b < n:
      c = a
      a = b
      b += c
    if n == b:
      return True
    return False  


# Test function để demo và giải thích
def test_fibonacci_demo():
    """
    Demo function để hiểu rõ hơn về Fibonacci và các cách tiếp cận
    """
    print("=" * 70)
    print("FIBONACCI NUMBER DEMO & EXPLANATION")
    print("=" * 70)
    
    solution = Solution()
    
    # Hiển thị dãy Fibonacci đầu tiên
    print("📚 Dãy Fibonacci đầu tiên:")
    a, b = 0, 1
    fib_sequence = [a]
    for _ in range(14):
        fib_sequence.append(b)
        a, b = b, a + b
    print(f"   {fib_sequence}")
    print(f"   Quy luật: F(n) = F(n-1) + F(n-2)")
    print(f"   Tăng trưởng: exponential (~φⁿ, φ ≈ 1.618 - Golden Ratio)")
    print()
    
    # Test một số cases
    print("🧪 Test Cases:")
    test_cases = [
        (0, "Fibonacci đầu tiên"),
        (1, "Fibonacci thứ 2 & 3"), 
        (4, "Không phải Fibonacci (giữa 3 và 5)"),
        (13, "Fibonacci thứ 8"),
        (14, "Không phải Fibonacci (giữa 13 và 21)"),
        (233, "Fibonacci lớn"),
        (234, "Không phải Fibonacci lớn")
    ]
    
    for n, description in test_cases:
        result = solution.isFibonacci(n)
        status = "✅ YES" if result else "❌ NO"
        print(f"   {n:>3} → {status} ({description})")
    
    print()
    print("💡 Tại sao Time Complexity là O(log n)?")
    print("   - Dãy Fibonacci tăng exponentially: F(n) ≈ φⁿ/√5")
    print("   - Để tìm F(k) = n, ta cần k ≈ log_φ(n) = O(log n)")
    print("   - Vì vậy chỉ cần ~log(n) iterations để generate đến n")
    
    print("\n🔧 Để thử các cách khác nhau:")
    print("   1. Mở file fibonacci.py")
    print("   2. Uncomment code trong function isFibonacci()")
    print("   3. Comment lại code hiện tại")
    print("   4. Chạy lại để so sánh performance!")


# Test riêng cho file này
if __name__ == "__main__":
    test_fibonacci_demo()

