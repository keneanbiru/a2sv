class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n  = len(nums)
        ans = 1

        inc = 1
        dec = 1

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                inc +=1
                dec = 1
            if nums[i] < nums[i-1]:
                dec+=1
                inc = 1
            if nums[i] == nums[i-1]:
                dec= 1 
                inc = 1
            
            ans = max(inc,dec,ans)
        return ans