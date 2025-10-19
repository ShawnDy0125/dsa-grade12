"""
Bài 5: Vẽ tam giác sao rỗng (Hollow Triangle)
Vẽ tam giác sao cân nhưng chỉ có viền, bên trong rỗng

Ví dụ với n=5:
    *
   * *
  *   *
 *     *
*********

Yêu cầu: Implement function printHollowTriangle(n) trả về list các dòng
"""


class Solution(object):
    def printHollowTriangle(self, n):
        """
        Vẽ tam giác sao rỗng với n dòng
        
        Args:
            n (int): Số dòng của tam giác
            
        Returns:
            list: Danh sách các dòng string chứa pattern tam giác rỗng
        
        Giải thích thuật toán:
        1. Dòng đầu tiên (i=1): chỉ có 1 sao ở giữa
        2. Dòng cuối cùng (i=n): toàn bộ sao như tam giác cân
        3. Các dòng giữa: chỉ có 2 sao ở hai đầu, giữa là spaces
        
        Pattern cho dòng i (1 < i < n):
        - (n - i) spaces đầu
        - 1 sao
        - (2 * i - 3) spaces giữa  
        - 1 sao (nếu i > 1)
        
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        """
        # TODO: Em hãy implement thuật toán ở đây
        # Gợi ý:
        # - Dòng 1: spaces + '*'
        # - Dòng cuối: spaces + toàn '*'
        # - Dòng giữa: spaces + '*' + spaces + '*'
        # Viết code ở đây

    
    def printHollowTriangleString(self, n):
        """
        Trả về tam giác dưới dạng string với newline
        """
        lines = self.printHollowTriangle(n)
        return '\n'.join(lines)


# Test riêng cho bài này  
if __name__ == "__main__":
    solution = Solution()
    
    print("Test Hollow Triangle với n=5:")
    result = solution.printHollowTriangle(5)
    for line in result:
        print(f"'{line}'")  # Dùng quotes để thấy rõ spaces
    
    print("\nTest với n=6:")
    result = solution.printHollowTriangle(6)
    for line in result:
        print(f"'{line}'")
        
    print("\nTest với n=1:")
    result = solution.printHollowTriangle(1)
    for line in result:
        print(f"'{line}'")
