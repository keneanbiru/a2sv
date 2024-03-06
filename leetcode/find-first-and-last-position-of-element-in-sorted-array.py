class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # left = -1
        # right = n
        count = Counter(nums)
        first_index = bisect.bisect_left(nums,target)
        print(first_index)
        if target not in nums:
            return [-1,-1]
        elif n==0  or first_index == n:
            return [-1,-1]
        elif first_index==0:
            return [0,count[nums[first_index]]-1]
        # elif first_index+1==n:
        #     return [first_index , first_index + count[nums[first_index]]-1]

        elif nums[first_index] == target :
            print(count[nums[first_index]])
            return [first_index , first_index + count[nums[first_index]]-1]
        return [-1,-1]

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if right==0:
        #     return [-1,-1]
        # if (len(set(nums))) == 1 :
        #     if target in nums:
        #         return [0,right-1]
        #     else:
        #         return[-1,-1]

        # while left+1 < right:
        #     mid = (left+right) // 2
        #     if (nums[mid] >= target):
        #         right = mid
        #     if (nums[mid] < target):
        #         left = mid
        
        # if (nums[right]==target):
        #     return [right ,right+(count[nums[left]])-1]
        # else:
        #     return[-1,-1]
        
         
