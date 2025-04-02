class Solution:
    def maximumTripletValue(self, nums):
        max_value = 0
        n = len(nums)

        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur = (nums[i] - nums[j]) * nums[k]
                    if cur > max_value:
                        max_value = cur

        return max_value if max_value > 0 else 0