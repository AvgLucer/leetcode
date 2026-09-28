class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False
        first_col = False

        #is 1st row zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row = True

        #is 1st column zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True
        
        
        #use 1st row and col as markers
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        #zero marked rows
        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(1,cols):
                    matrix[i][j] = 0
        
        #zero marked columns

        for j in range(1,cols):
            if matrix[0][j] == 0:
                for i in range(1,rows):
                    matrix[i][j] = 0

        #zero first row
        if first_row:
            for j in range(cols):
                matrix[0][j]=0
            
        #zero first column
        if first_col:
            for i in range(rows):
                matrix[i][0]=0


