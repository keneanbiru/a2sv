class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:    
        # req = []
        # set1 = set()
        ans = [0]*(len(nums)+1)
        pre = res = 0
        # for i in requests:
        #     set1.add(i[0])
        #     set1.add(i[1])
        # list1 = list(set1)
        # maxi = max(list1)
        # for i in requests:
        #     list1 = list(range(i[0],i[1]+1))
        #     req.extend(list1)
        # count = Counter(req)
        # # print(count)
        # sortted = sorted(count.items(),key = lambda i:i[1],reverse = True)
        # # print(sortted)
        # # for key, val in count.items():
        # nums.sort()
        # for i in sortted:
        #     i = list(i)
        #     if nums:
        #         ans[i[0]] = nums.pop()

        for i in requests:
            ans[i[0]] +=1
            ans[i[1]+1] -=1
        print(ans)


        for i in range(len(ans)):
            pre += ans[i]
            ans[i] = pre
        print(ans)
        ans = sorted(ans,reverse=True)
        nums = sorted(nums,reverse=True)
        res = 0
        i = 0
        while i<len(nums):
            res+=nums[i]*ans[i]
            i+=1
        return res%(10**9+7)

        # print(ans)
        # for i in requests:
        #     if i[0]==0:
        #         res += ans[i[1]]
        #     else:
        #         res += ans[i[1]] - ans[i[0]-1]
        # return res
           



            
        # print(req)
        # return 1

        