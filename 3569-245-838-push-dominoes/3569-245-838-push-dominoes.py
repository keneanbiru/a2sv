class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        right = []
        left = []
        l,r = 0,0
        
        while l < n:
            if d[l] == "L":
                right.append(0)
                
                l+=1
                r+=1
            elif d[l] == "R":
                r+=1
                while r < n and d[r] == ".":
                    r+=1
                
                dif = r-l
                for i in range(dif,0,-1):
                    right.append(i)
                if dif == 0:
                    l+=1
                    r+=1
                l = r
            else:
                right.append(0)
                l+=1
                r+=1

        
        l,r = n-1,n-1

        while l > -1:
            if d[r] == "R":
                left.append(0)
                
                l-=1
                r-=1
            elif d[r] == "L":
                l-=1
                while l > -1 and d[l] == ".":
                    l-=1
                
                dif = r-l
                for i in range(dif,0,-1):
                    left.append(i)
                if dif == 0:
                    l-=1
                    r-=1
                r = l
            else:
                left.append(0)
                l-=1
                r-=1
        
        ans = ""
        left.reverse()

        for i in range(len(right)):
            if right[i] > left[i]:
                ans += "R"
            elif left[i] > right[i]:
                ans += "L"
            else:
                ans += "."
        return ans
        
        
               