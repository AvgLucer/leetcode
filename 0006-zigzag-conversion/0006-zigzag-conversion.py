class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s

        currentrow =0
        rows = [""] * numRows
        direction = 1

        for ch in s:

            rows[currentrow] += ch
            if currentrow == 0:
                direction = 1
            elif currentrow == numRows -1:
                direction = -1

            currentrow += direction
        return "".join(rows)
        
