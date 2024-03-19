class Solution:
    def minProcessingTime(self, processorTime: List[int], nums: List[int]) -> int:
        processorTime = sorted(processorTime,reverse = True)
        n = len(nums)
        nums.sort()
        # q  = n//4
        i= 4
        j = 0
        maxi = 0
        while j <len(processorTime) and i<= len(nums):
            maxi  = max(max(nums[i-4:i]) + processorTime[j],maxi)           
            i +=4
            j += 1
        return maxi




        
        