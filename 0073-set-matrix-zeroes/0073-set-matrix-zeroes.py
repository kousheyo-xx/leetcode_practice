class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        R,C=False,False
        for i in range(m):
            if matrix[i][0]==0:
                C=True
        for j in range(n):
            if matrix[0][j]==0:
                R=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if R:
            for j in range(n):
                matrix[0][j]=0
        if C:
            for i in range(m):
                matrix[i][0]=0