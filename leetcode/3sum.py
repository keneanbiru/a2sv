class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mid = i
            l = mid+1
            r = n-1
            #    print(nums[i])
            while l<r:
                
                if nums[l]+nums[r]+nums[mid]==0:
                    
                    ans.add((nums[l],nums[r],nums[mid]))
                    r-=1
                    l+=1
                elif nums[l]+nums[r]+nums[mid]<0:
                    l+=1
                else:
                    r-=1
        return list(ans)
