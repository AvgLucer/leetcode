class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        for string in s.split():
            stack.append(string)
        
        stack.reverse()

        return " ".join(stack)