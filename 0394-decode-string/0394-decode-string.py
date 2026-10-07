class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []
        strstack = []

        num = 0
        
        current = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char == "[":
                numstack.append(num)
                strstack.append(current)

                num = 0
                current = ""
            
            elif char == "]":
                repeat = numstack.pop()
                previous = strstack.pop()

                current = previous  + current * repeat
            
            else:
                current += char

        return current
