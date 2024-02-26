class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half_pow = pow(x,n//2)
        if n%2 :
            return (half_pow * half_pow * x )
        return (half_pow*half_pow)