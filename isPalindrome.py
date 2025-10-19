class Solution(object):
    def isPalindrome(self, x):
        result = str(x)
        return result[::-1] == result