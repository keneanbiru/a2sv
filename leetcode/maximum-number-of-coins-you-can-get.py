class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0 
        n = len(piles)
        q = n/3
        i = 0
        piles.sort()
        ans = 0
        while i<q:
            piles.pop()
            ans += piles.pop()
            i+=1
        return ans
            
            

        