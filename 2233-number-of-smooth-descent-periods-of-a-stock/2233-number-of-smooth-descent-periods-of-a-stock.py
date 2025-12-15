class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in range(len(prices)-1):
            if prices[i+1] == prices[i] - 1:
                cnt+=1
            else:
                if cnt>0:
                    cnt+=1
                ans += (cnt*(cnt - 1)) // 2
                cnt = 0
        if cnt>0:
            cnt+=1
        ans += (cnt*(cnt - 1)) // 2
        return ans + len(prices)

