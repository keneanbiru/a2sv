class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n=len(nums)
        @cache
        def fun(i, c):
            if i==n:
                if c==1: return -(1<<31)
                return 0
            x=nums[i]
            return max(x+fun(i+1, c),(x^k)+fun(i+1,1-c))
        return fun(0, 0)
        