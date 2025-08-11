class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power = []
        num = n

        for i in range(30,-1,-1):
            if num >= 2**i:
                power.append(i)
                num-=2**i
            
        power.reverse()
        ans = []
        
        for i,j in queries:
            cur = 0
            for k in range(i,j+1):
                cur += power[k]
            ans.append(2**cur %( 10**9 + 7))


        return ans
        

        