class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(l,r):
            if l==r:
                return nums[l]
            left = nums[l] - rec(l+1,r)
            right = nums[r] - rec(l,r-1)
            return max(left,right)
        return rec(0,len(nums)-1) >= 0 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #     if i==j:
        #         if turn :
        #             return[[nums[i],0]]
        #         else :
        #             return [0,nums[j]]
        #     left=rec(i+1,j,not turn)
        #     right=rec(i,j-1,not turn)
        #     if turn:
            
        #         if (left[0]+nums[i]-left[1] > right[0]+nums[j]-right[1]):
        #             left[0] +=nums[i]
        #             return left
        #         else:
        #             right[0]+=nums[j]
        #             return right
        # list1=rec(0,len(nums)-1,True)
        # if (list1[0]>list1[1]):
        #     return True
        # else:
        #     return False
