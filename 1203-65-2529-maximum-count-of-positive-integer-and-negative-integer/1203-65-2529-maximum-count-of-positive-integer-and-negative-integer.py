class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        right = 0 
        while right < len(nums) and nums[right] < 0:
            right  += 1
        left = right
        while left < len(nums) and nums[left] == 0:
            left+=1
        # print(left,right)
        return max(right  ,len(nums) - left)
