class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        s_org=s
        res=0
        odds=[]
        s=list(set(s))
        print(s)
        if (len(s)==1):
            return len(s_org)
        for i in s:
            if count[i]%2==0:
                res+=count[i]
                print(res)
            else:
                odds.append(count[i])
        if  odds:
            res=res+(sum(odds)-(len(odds)-1))
        return res
