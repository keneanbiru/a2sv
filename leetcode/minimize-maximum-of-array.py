class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s,a=0,0
        avg=0
        for i in range(len(nums)):
            s=s+nums[i]
            avg=s/(i+1)
            # print(avg)
            if avg>a:
                a=avg
        return ceil(a)

        
        
        
        
        
        
        # TLE

        # n=len(nums)
        # max1=max(nums)
        # index1=nums.index(max1)
        # max2=max1
        # while (max2>=max1 and index1!=0):
        #     max2=max1
        #     nums[index1]-=1
        #     nums[index1-1]+=1
        #     #print(nums)
        #     max1=max(nums)
        #     index1=nums.index(max1)



    
        return nums[index1]

        