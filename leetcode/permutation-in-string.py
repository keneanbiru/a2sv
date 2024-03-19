class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        c1 = Counter(s1)
        c2 = Counter(s2[0:n1])
        l = 0
        r = l+n1
        while r<n2:
            if c1 == c2:
                return True
            c2[s2[l]]-=1
            if c2[s2[l]] == 0:
                del c2[s2[l]]
            
            if c2[s2[r]]:
                c2[s2[r]] += 1
            else:
                c2[s2[r]] = 1
            l+=1
            r+=1
        if c1==c2:
            return True
        return False



