class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left = 0
        # right =  len(nums)
        # maxi=max(nums)
        # if (target > maxi):
        #     return len(nums)
        # mid =0 
        # while left < right:
        #     mid = (left+right)//2
            
        #     if (target > nums[mid]):
        #         left = mid+1
        #     elif (target < nums[mid]):
        #         right = mid-1
        #     elif(target == nums[mid]):
        #         return mid
        
        # return left
        
        index = bisect.bisect_left(nums,target)
        return (index)

        