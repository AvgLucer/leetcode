#from collections import Counter                # Easier method

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)       # Easier method

        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for c in s:
            count[c] = count.get(c, 0) + 1

        # Remove counts using t
        for c in t:
            if c not in count:
                return False

            count[c] -= 1

            if count[c] < 0:
                return False

        return True