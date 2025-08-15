class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0 :
            return False
        power = math.log2(n)
        
        if power == int(power) and power % 2 == 0:
            return True
        return False
            