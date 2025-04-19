class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            dif1 = lower - nums[i]
            dif2 = upper - nums[i]
            idx1 = bisect.bisect_left(nums , dif1 , i+1)
            idx2 = bisect.bisect_right(nums , dif2 ,i+1)
            ans+=idx2 -idx1
        return ans