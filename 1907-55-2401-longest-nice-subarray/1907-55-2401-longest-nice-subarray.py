class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        maskk=0
        maxi=0
        i=0 
        for j in range(len(nums)): 
            while((maskk & nums[j])!=0):
                maskk^=nums[i]  
                i+=1
            maskk |=nums[j]
            maxi=max(maxi,j-i+1)
        
        return maxi