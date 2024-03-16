class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n= len(nums)
        pre =0 
        prefix = [0]*(n+1)
        ans= [0]*n
        for i in range(n):
            pre += nums[i]
            prefix[i] = pre
        # print(prefix)
        for i in range (n):
            ans[i] = ((nums[i]*i)-prefix[i-1])+ ((prefix[n-1]-prefix[i]) - (nums[i]*(n-1-i)))
            # print(ans[i])
        return ans

