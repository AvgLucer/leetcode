class Solution:
    def myAtoi(self, s: str) -> int:
        output = 0
        sign = 1
        seen_digit = False
        for char in s:
            if char.isdigit():
                seen_digit = True
                output = output * 10 + int(char)
            elif char == '-' and not seen_digit and not seen_digit:
                sign = -1
                seen_digit = True
            elif char == '+' and not seen_digit and not seen_digit:
                sign = 1
                seen_digit = True

            elif char == ' ' and not seen_digit and not seen_digit:
                continue
            else:
                break
        works = output * sign
        if works < -2147483648:
            return -2147483648

        elif works > 2147483647:
            return 2147483647
        

        return works
    
