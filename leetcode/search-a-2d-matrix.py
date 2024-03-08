class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # index = (row_index * number_of_columns) + column_index
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = (row * col) -1
        def convert_2D_to_1D(two_d_array):
            one_d_array = []
            for row in two_d_array:
                one_d_array.extend(row)
            return one_d_array
        arr =   convert_2D_to_1D(matrix)  
        print(arr)
        index = 0

        while left <= right:
            # index = (row * col) + column_index
            mid = (left + right)//2
            if target == arr[mid ] :
                return True
            elif (target < arr[mid] ):
                right = mid-1
            elif (target > arr[mid]):
                left = mid +1
        return False


     