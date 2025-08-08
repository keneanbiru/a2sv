class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500:
            return 1
        memo = dict()
        def dp(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            if x<=0 and y<=0:
                return 0.5
            elif x <= 0:
                return 1
            elif y<=0:
                return 0
            memo[(x,y)] = 0.25 * (dp(x -100 , y) + dp (x - 75 , y -25) + dp (x - 50 , y - 50) + dp (x - 25 , y - 75))
            return memo[(x,y)]
        
        return dp(n , n)

        