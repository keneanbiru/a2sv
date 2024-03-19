class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ["a","e","i","o","u"]
        count = 0
        n = len(s)
        
        for i in range (k):
            if s[i] in v:
                count +=1
       
        maxi = count
        l = 0
        r = l+k
        while r<n:
            if s[r] in v:
                count+=1
            if s[l] in v:
                count-=1
            
            maxi = max(count,maxi)
            l+=1
            r+=1
        return maxi
