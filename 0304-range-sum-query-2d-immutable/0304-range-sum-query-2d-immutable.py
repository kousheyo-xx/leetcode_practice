class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.prefix=[[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            preSum=0
            for j in range(col):
                preSum+=matrix[i][j]
                self.prefix[i+1][j+1]=preSum+self.prefix[i][j+1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight=self.prefix[row2+1][col2+1]
        left=self.prefix[row2+1][col1]
        top=self.prefix[row1][col2+1]
        topLeft=self.prefix[row1][col1]
        return bottomRight-left-top+topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)