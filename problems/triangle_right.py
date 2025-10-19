"""
Bài 3: Vẽ tam giác sao vuông (Right Triangle)
Vẽ tam giác sao với cạnh góc vuông bên trái

Ví dụ với n=5:
*
**
***
****
*****

Yêu cầu: Implement function printRightTriangle(n) trả về list các dòng
"""


class Solution(object):
    def printRightTriangle(self, n):
        """
        Vẽ tam giác sao vuông với n dòng
        
        Args:
            n (int): Số dòng của tam giác
            
        Returns:
            list: Danh sách các dòng string chứa pattern tam giác
        
        Giải thích thuật toán:
        1. Duyệt từ dòng 1 đến n
        2. Mỗi dòng i có i ký tự sao (*)
        3. Không có khoảng trắng đầu dòng
        
        Time Complexity: O(n²) - tạo n dòng, mỗi dòng có tối đa n ký tự
        Space Complexity: O(n²) - lưu tất cả các dòng
        """
        # TODO: Em hãy implement thuật toán ở đây
        # Gợi ý: Dùng vòng lặp for từ 1 đến n+1, mỗi lần append i ký tự '*'
        # Viết code ở đây

    
    def printRightTriangleString(self, n):
        """
        Trả về tam giác dưới dạng string với newline
        """
        lines = self.printRightTriangle(n)
        return '\n'.join(lines)


# Test riêng cho bài này
if __name__ == "__main__":
    solution = Solution()
    
    print("Test Right Triangle với n=5:")
    result = solution.printRightTriangle(5)
    for line in result:
        print(line)
    
    print("\nTest với n=3:")
    result = solution.printRightTriangle(3)
    for line in result:
        print(line)
