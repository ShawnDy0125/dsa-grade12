"""
Bài 1: Kiểm tra số Palindrome
Palindrome là số đọc từ trái sang phải và từ phải sang trái đều giống nhau.

Ví dụ:
- 121 là palindrome
- -121 không phải palindrome (vì dấu âm)
- 10 không phải palindrome

Yêu cầu: Implement function isPalindrome(x) trả về True/False
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        Kiểm tra số x có phải palindrome không
        
        Args:
            x (int): Số cần kiểm tra
            
        Returns:
            bool: True nếu là palindrome, False nếu không
        
        Có 3 cách approach khác nhau - Em hãy chọn 1 cách để implement:
        
        CÁCH 1 - STRING SLICING (Dễ hiểu nhất):
        ======================================
        - Chuyển số thành string và so sánh với string đảo ngược
        - Time: O(n) với n là số chữ số
        - Space: O(n) để store string
        - Thuật toán:
          1. Convert x thành string: s = str(x)
          2. So sánh s với s[::-1] (string đảo ngược)
          3. Return kết quả
        
        CÁCH 2 - MATH ONLY (Không dùng string):
        =======================================  
        - Đảo ngược số bằng phép toán, không dùng string
        - Time: O(log n) với n là giá trị của số
        - Space: O(1)
        - Thuật toán:
          1. Số âm return False
          2. Lưu original = x
          3. Build reversed number: digit = x % 10, reversed = reversed * 10 + digit
          4. So sánh original == reversed
        
        CÁCH 3 - OPTIMIZED (Chỉ reverse một nửa):
        ========================================
        - Chỉ đảo ngược nửa số, so sánh với nửa còn lại
        - Time: O(log n / 2) - nhanh hơn cách 2
        - Space: O(1)  
        - Thuật toán:
          1. Handle edge cases: x < 0 hoặc x % 10 == 0 (trừ x == 0)
          2. Reverse cho đến khi x <= reversed_half
          3. Check x == reversed_half (even digits) hoặc x == reversed_half // 10 (odd digits)
        """
        
        # TODO: Em hãy chọn 1 trong 3 cách trên để implement
        
        # ============ CÁCH 1: STRING SLICING ============
        # Uncomment code dưới để dùng cách 1:
        """
        s = str(x)
        return s == s[::-1]
        """
        
        # ============ CÁCH 2: MATH ONLY ============
        # Uncomment code dưới để dùng cách 2:
        """
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num
        """
        
        # ============ CÁCH 3: OPTIMIZED HALF-REVERSE ============
        # Uncomment code dưới để dùng cách 3:
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10
        """
        
        # ============ DEFAULT IMPLEMENTATION ============
        # Hiện tại dùng cách 1 (String Slicing) làm mặc định:
        # TODO: Implement ở đây
        # Viết code ở đây



# Test function để demo và giải thích  
def test_palindrome_demo():
    """
    Demo function để hiểu rõ hơn về Palindrome và các cách tiếp cận
    """
    print("=" * 60)
    print("PALINDROME DEMO & EXPLANATION")
    print("=" * 60)
    
    solution = Solution()
    
    # Giải thích palindrome
    print("📚 Palindrome là gì?")
    print("   - Số đọc từ trái sang phải = từ phải sang trái")
    print("   - Ví dụ: 121, 1221, 12321")
    print("   - Số âm KHÔNG BAO GIỜ là palindrome (vì dấu -)")
    print()
    
    # Test cases với giải thích
    print("🧪 Test Cases:")
    test_cases = [
        (121, "Palindrome đơn giản 3 chữ số"),
        (-121, "Số âm → False (vì dấu -)"),
        (10, "Số có 0 cuối → False"),
        (0, "Số 0 → True"), 
        (1221, "Palindrome chẵn chữ số"),
        (12321, "Palindrome lẻ chữ số"),
        (123321, "Palindrome 6 chữ số"),
        (1234321, "Palindrome 7 chữ số"),
        (999, "Tất cả chữ số giống nhau")
    ]
    
    for x, description in test_cases:
        result = solution.isPalindrome(x)
        status = "✅ YES" if result else "❌ NO"
        
        # Demo reverse process
        if x >= 0:
            s = str(x)
            reversed_s = s[::-1]
            print(f"   {x:>7} → {status} ({description})")
            print(f"          String: '{s}' vs '{reversed_s}'")
        else:
            print(f"   {x:>7} → {status} ({description})")
        print()
    
    print("💡 So sánh 3 cách approach:")
    print("   CÁCH 1 - String: Dễ hiểu, code ngắn, nhưng dùng extra memory")
    print("   CÁCH 2 - Math: Không dùng string, memory efficient") 
    print("   CÁCH 3 - Optimized: Chỉ check một nửa, fastest execution")
    
    print("\n🔧 Để thử các cách khác nhau:")
    print("   1. Mở file palindrome.py") 
    print("   2. Uncomment code trong function isPalindrome()")
    print("   3. Comment lại code hiện tại")
    print("   4. Chạy lại để so sánh performance!")
    
    print(f"\n📊 Ví dụ step-by-step cho x = 12321:")
    print("   Cách 1: '12321' == '12321'[::-1] == '12321' → True")
    print("   Cách 2: reverse(12321) = 12321 == 12321 → True")
    print("   Cách 3: 12321 → 123 vs 123 (chỉ cần check một nửa)")


# Test riêng cho file này
if __name__ == "__main__":
    test_palindrome_demo()
