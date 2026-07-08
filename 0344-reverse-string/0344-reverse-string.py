class Solution:
    def reverseString(self, s: List[str]) -> None:
        def fun(s,l,r):
            if l > r: 
                return 
            
            s[l],s[r] = s[r],s[l]
            return fun(s,l+1,r-1)
        return fun(s,0,len(s)-1)
        