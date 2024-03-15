class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        rows,cols = len(self.matrix) ,len(self.matrix[0])
        self.submat = [[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows):
            prefix = 0
            for j in range (cols):
                prefix += matrix[i][j]
                above = self.submat[i][j+1]
                self.submat[i+1][j+1] = prefix +above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            res = self.submat[row2+1][col2+1] - self.submat[row1][col2+1] - self.submat[row2+1][col1]  +self.submat[row1][col1]
            return res

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)