class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sett = set(nums)

        nums1 = list(sett)
        nums1.sort(reverse = True)
        ans = 0
        if nums1[0]<=0:
            return nums1[0]
        for i in nums1:
            if i > 0:
                ans+=i

            else:
                return ans
    
        
        return ans
       