class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if j>i:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(m//2):
                matrix[i][m-j-1],matrix[i][j]=matrix[i][j],matrix[i][m-j-1]