"""
Bài 4: Vẽ tam giác sao cân (Isosceles Triangle)
Vẽ tam giác sao cân với đỉnh ở trên

Ví dụ với n=5:
    *
   ***
  *****
 *******
*********

Yêu cầu: Implement function printIsoscelesTriangle(n) trả về list các dòng
"""


class Solution(object):
    def printIsoscelesTriangle(self, n):
        """
        Vẽ tam giác sao cân với n dòng
        
        Args:
            n (int): Số dòng của tam giác
            
        Returns:
            list: Danh sách các dòng string chứa pattern tam giác cân
        
        Giải thích thuật toán:
        1. Duyệt từ dòng 1 đến n
        2. Dòng i có:
           - (n - i) khoảng trắng đầu
           - (2 * i - 1) ký tự sao
        3. Pattern: spaces + stars
        
        Ví dụ n=5:
        - Dòng 1: 4 spaces + 1 star
        - Dòng 2: 3 spaces + 3 stars  
        - Dòng 3: 2 spaces + 5 stars
        - Dòng 4: 1 space + 7 stars
        - Dòng 5: 0 spaces + 9 stars
        
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        """
        # TODO: Em hãy implement thuật toán ở đây
        # Gợi ý: 
        # - Số spaces = n - i
        # - Số stars = 2 * i - 1
        # - Kết hợp: ' ' * spaces + '*' * stars
        # Viết code ở đây
class Solution(object):
    def printIsoscelesTriangle(self,n):
        result = [ ]
        for i in range(1, n + 1):
            blank = n - i 
            star = 2 * i - 1
            print(" " * blank +"*" * star)
            result.append(" " * blank + "*" * star)
        return result
        
    
    def printIsoscelesTriangleString(self, n):
        """
        Trả về tam giác dưới dạng string với newline
        """
        lines = self.printIsoscelesTriangle(n)
        return '\n'.join(lines)


# Test riêng cho bài này
if __name__ == "__main__":
    solution = Solution()
    
    print("Test Isosceles Triangle với n=5:")
    result = solution.printIsoscelesTriangle(5)
    for line in result:
        print(f"'{line}'")  # Dùng quotes để thấy rõ spaces
    
    print("\nTest với n=4:")
    result = solution.printIsoscelesTriangle(4)
    for line in result:
        print(f"'{line}'")
