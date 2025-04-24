class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans  = 0
        sett = set(nums)
        n = len(sett)
        cnt = dict()
        l = 0
        r = 0
        while l < len(nums):
           
            if nums[r] in cnt:
                cnt[nums[r]] +=1
            else:
                cnt[nums[r]] = 1
            
            while len(cnt) == n:
                ans+=len(nums )- r
                cnt[nums[l]] -=1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l+=1
                
            if r < len(nums)-1:
                r+=1
            else:
                break
        return ans
                