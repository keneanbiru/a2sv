class Solution:
    def largestDivisibleSubset(self, nums):
        
        nums.sort()
        n = len(nums)

        
        dp = [1] * n

        
        maxis = 1
        maxii = 0

        
        for i in range(1, n):
            for j in range(i):
                
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

            
            if dp[i] > maxis:
                maxis = dp[i]
                maxii = i


        result = []
        current_num = nums[maxii]
        current_size = maxis

        for i in range(maxii, -1, -1):
            #
            
            if current_num % nums[i] == 0 and dp[i] == current_size:
                result.append(nums[i])
                current_num = nums[i]
                current_size -= 1

        
        result.reverse()
        return result
