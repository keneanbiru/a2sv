class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pre = [0]
        ans = 0
        for i in arr:
            pre.append(pre[-1] + i)
            if pre[-1] % 2!= 0 :
                ans+=1
        even = 0
        odd = 0
        # print(ans,pre)
        for i in range(1,len(pre)):
            # print(ans,even,odd)
            if pre[i] %2 == 0:
                ans+=odd
                even+=1
            else:
                ans+=even
                odd+=1
        return ans%(10**9+7)

               