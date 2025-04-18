class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n==1:
            return "1"
        ans = []
        for i in range(2,n+1):
            # print(s)
            ans = []
            now = s[0]
            cnt = 0
            for i in s:
                if i == now:
                    cnt+=1
                else:
                    ans.append(str(cnt))
                    ans.append(now)
                    now = i
                    cnt = 1
            ans.append(str(cnt))
            ans.append(now)
            s = "".join(ans)
        # print(ans)






        return "".join(ans)





        