class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        ans = float("inf")

        for r in range(len(nums)):
            summ+=nums[r]
            while summ >= target:
                ans = min(ans,r-l+1)
                summ-=nums[l]
                l+=1
        return 0 if ans == float("inf") else ans


        