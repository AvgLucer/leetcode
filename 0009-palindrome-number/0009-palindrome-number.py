res = 0
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        res = str(x) == str(x)[::-1]
        return bool(res)