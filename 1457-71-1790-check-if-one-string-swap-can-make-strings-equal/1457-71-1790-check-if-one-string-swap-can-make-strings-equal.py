class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        l = 0
        n = len(s1)
        dif = 0
        idx = []
        
        while l < n:
            if s1[l] != s2[l]:
                idx.append(l)
                dif+=1
            if dif > 2:
                return False
            l+=1
        if dif == 2 and s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]:
            return True
        return False


        