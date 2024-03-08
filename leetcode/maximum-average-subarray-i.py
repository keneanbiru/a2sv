class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = l+k
     
        
        if len(nums)==1:
            return float(nums[0])
        sum1 = sum(nums[l:r])
        avg = sum1/k
        maxi= avg
        print(sum1)
        
        
        while r<len(nums):
        
            print(nums[l],nums[r])
            sum1 = ((sum1 -nums[l]) + nums[r])
            avg = sum1/k
            r+=1
            l+=1
            maxi = max(maxi,avg)
            
        # print(arr)
        return maxi
        