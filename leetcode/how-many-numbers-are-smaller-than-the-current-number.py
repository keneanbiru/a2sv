class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # s = sorted(nums)
        # i = 0
        # n = len(nums)
        # dict1 =  {}
        # for i,j in enumerate(s):
            

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        n=len(nums)
        sorrted = sorted(nums)
        dict1 = defaultdict()
        ans = []
        for i in range(len(sorrted)-1,-1,-1):
            dict1[sorrted[i]] = i
        for i in nums:
            ans.append(dict1[i])
        return ans

       

            
