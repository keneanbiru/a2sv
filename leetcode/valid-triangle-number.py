class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        count=0
        n=len(nums)
        for i in range(n-1,1,-1):
            l=0
            r=i-1
            while(l<r):
                if (nums[l]+nums[r]>nums[i]):
                    count+=r-l
                    r-=1
                else:
                   
                    l+=1
        return count
            

