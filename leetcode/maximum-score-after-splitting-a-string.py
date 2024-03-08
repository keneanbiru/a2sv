class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        r = s.count("1")
        maxi = -1
        for i in range(len(s)-1):
            if s[i] == "1":
                r-=1
            else:
                l+=1
            maxi = max(maxi,l+r)
        return maxi

