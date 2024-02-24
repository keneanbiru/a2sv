class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[[0]*len(matrix) for _ in range (len(matrix[0]))]
        rlen =len(matrix)
        clen=len(matrix[0])
        for i in range (rlen):
            for j in range(clen):
                transposed[j][i]=matrix[i][j]
        return transposed

        