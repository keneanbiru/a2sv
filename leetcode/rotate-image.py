class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zipped=list(zip(*matrix))
       
        for i in range(len(zipped)):
            x=reversed(list(zipped[i]))
            matrix[i]=x

        