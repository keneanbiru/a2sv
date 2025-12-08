class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n):
            for j in range(1,n):
                c =  sqrt(i*i + j*j)
                # print(c)
                if c == int(c) and c <=n:
                    ans+=1
        return ans





        