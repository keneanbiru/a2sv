class Solution:
    def canJump(self, nums: List[int]) -> bool:
    #    cur=0
    #    for i in range(len(nums)-1):
    #        cur=max(cur-1,i)

            
        n = len(nums)
        g = n - 1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= g:
                g = i

        return g == 0