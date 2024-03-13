class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i = 0
        sum_ = max_ = 0
        for j in range(len(nums)):
            sum_ += nums[j]
            while (j - i + 1) - sum_ > 1:
                sum_ -= nums[i]
                i += 1
            max_ = max(max_, j - i)
        return max_
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l = 0
        # maxi = 0
        # cur = 0
        # setted = set(nums)
        # if len(setted) == sum(setted):
        #     return len(nums)-1
        # elif len(setted) == 1 and 0 in setted:
        #     return 0
        # def valid(arr):
        #     if len(arr) - sum(arr) > 1:
        #         return False
        #     return True

        # for r in range(len(nums)):
            
        #     if not valid(nums[l:r]):
        #         maxi= max(cur,maxi)
        #         cur = 0
        #         while not valid(nums[l:r]):
        #             l+=1
        #         continue
        #     maxi= max(cur,maxi)
        #     cur+=1
            
        # return maxi
            

               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # while r<len(nums):
        # #     if len(nums[l:r])-1 <= sum(nums[l:r]):
        # #         print(sum(nums[l:r]))
        # #         cur +=1
        # #         r+=1
        # #     else:
        # #         print("x")
        # #         maxi=max(maxi,cur)
        # #         while len(nums[l:r])-1 != sum(nums[l:r]):
        # #             l+=1
        # #         cur = 0
        # # return maxi
                

        