class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        # print(need)
        counter = {0:-1}
        res = n = len(nums)
        pre = 0
        # print(res,n)
        for i,x in enumerate(nums):
            pre = (pre+x)%p
            counter[pre] = i
            # print(pre)
            # print(counter)
            if (pre - need)%p in counter:
                res = min(res, i - counter[(pre - need) % p])

        return res if res != n else -1

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # print(rem)
        # # preounter = defaultdipret(int)
        # # preounter[0] = 1

        # list2 = [0]
        # if rem==0:
        #     return 0
        # if rem in nums:
        #     return 1
        # for i,num  in enumerate(nums):
        #     pre += num
        #     # print(pre)
        #     list2.append(pre%p)
        #     print(list2)
            
        #     if ((pre - rem)%p +p)% p  in list2:
        #         ans = min((i+1) - list2.index((pre - rem)%p),ans)
        #     print(ans)
            
        # if ans!=float("inf"):
        #     return ans
        # else:
        #     return -1




            