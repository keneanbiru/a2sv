class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxi = 1
        ans = []
        if nums.count(0)>1:
            return [0]*len(nums)
        for i in nums:
            if i !=0:
                maxi*=i
        
        if  0 in nums:
            for i in nums :
                if i == 0:
                    ans.append(maxi)
                else:
                    ans.append(0)
        else:
            for i in nums:
                ans.append(int(maxi/i))
        return ans
