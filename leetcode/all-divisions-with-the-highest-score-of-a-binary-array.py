class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # l=0
        # r=nums.count(1)
        # # if r==len(nums):
        # #     return 
        # dic1={}
        # dic1[0]=l+r

        # for i in range(len (nums)):
        #     if nums[i]==0:
        #         l+=1
        #     else :
        #         r-=1
        #     dic1[i+1]=l+r
        # print(dic1)
        # dic1=dict(sorted(dic1.items(),key=lambda item :item[1],reverse=True))
       
        # list1=list(dic1.values())
        # list2=[]
        # max1=max(list1)
        # for key ,value in dic1.items():
        #     if value==max1:
        #         list2.append(key)
        #     else :
        #         break
            
        # return list2
       
        one_count=nums.count(1)
        cur_zero=0
        max1=one_count
        if one_count==len(nums):
            return [0]
        list1=[]
        for i in range(len(nums)+1):
            res=cur_zero+one_count
            # print(res)
            if max1<res:
                # print("y", i)
                max1=res
                list1=[i]
            elif max1==res:
                # print("x", i)
                list1.append(i)

            if  i < len(nums) and nums[i]==0:
                cur_zero+=1
            else:
                one_count-=1
            
            
            
        return list1

