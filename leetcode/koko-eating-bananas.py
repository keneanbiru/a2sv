class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def fun(mid):
            summ = 0
            for i in range(len(piles)):
                summ += ceil(piles[i]/mid)
            return summ

        left = 0
        right = max(piles)
        while left + 1< right:
            mid = (left + right)//2
            if fun(mid) > h:
                left = mid
            else:
                right = mid
                
        return right