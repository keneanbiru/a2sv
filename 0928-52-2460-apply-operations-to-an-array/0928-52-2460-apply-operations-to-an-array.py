
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift zeros to the end (in-place)
        idx = 0
        
        # Move all non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        
        # Fill the remaining positions with zeros
        for i in range(idx, n):
            nums[i] = 0
        
        return nums
        