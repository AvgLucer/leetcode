class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted1 = "".join(sorted(s))
        sorted2 = "".join(sorted(t))
        if sorted1 == sorted2:
            return True
        return False