class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n

        cnt = [0] * (size + 1)
        
        for i in range(n):
            for j in range(n):
                cnt[grid[i][j]] += 1

        a, b = -1, -1
        
        for num in range(1, size + 1):
            if cnt[num] == 2:
                a = num
            elif cnt[num] == 0:
                b = num
                
        return [a, b]