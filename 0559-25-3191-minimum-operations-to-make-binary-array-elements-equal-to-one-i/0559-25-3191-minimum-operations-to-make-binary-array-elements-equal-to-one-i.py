class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i+1] == 0:
                    nums[i+1] = 1
                else:
                    nums[i+1] = 0

                if nums[i+2] == 0:
                    nums[i+2] = 1
                else:
                    nums[i+2] = 0
                ans+=1
        if nums[-1]==0  or nums[-2]==0:
            return -1
        return ans
        