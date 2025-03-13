class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        left, right = 0, len(queries)

        if not self.canMakeZero(nums, queries, right):
            return -1

        while left < right:
            mid = (left + right) // 2
            if self.canMakeZero(nums, queries, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canMakeZero(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        prefix = 0
        diff = [0] * (n + 1)

        for i in range(k):
            start, end, val = queries[i]
            diff[start] += val
            diff[end + 1] -= val

        for i in range(n):
            prefix += diff[i]
            if prefix < nums[i]:
                return False

        return True
