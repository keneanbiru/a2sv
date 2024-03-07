class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = (left+right)//2
            # print(nums[left])
            # print(nums[right])
            # print(nums[mid])
            if  nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            
        
            
    #     low = 0
    #     high = len(nums) -1
        
        
    #     if nums[low] <= nums[high]: 
    #         return nums[low] 
  
    # # Binary search 
    #     while low <= high: 
    #         mid = (low + high) // 2
    
    #         # Check if mid is the minimum element 
    #         if nums[mid] < nums[mid-1]: 
    #             return nums[mid] 
    #         # If the left half is sorted, the minimum element must be in the right half 
    #         if nums[mid] > nums[high]: 
    #             low = mid + 1
    
    #         # If the right half is sorted, the minimum element must be in the left half 
    #         else: 
    #             high = mid - 1
