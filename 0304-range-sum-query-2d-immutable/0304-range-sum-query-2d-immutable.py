class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.preSum=[[0]*(col+1) for _ in range (row+1)]
        for i in range(1,row+1):
            prefix=0
            for j in range(1,col+1):
                prefix+=matrix[i-1][j-1]
                above=self.preSum[i-1][j]
                self.preSum[i][j]=prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight=self.preSum[row2+1][col2+1]
        left=self.preSum[row1][col2+1]
        top=self.preSum[row2+1][col1]
        topLeft=self.preSum[row1][col1]
        return bottomRight-left-top+topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)