class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if (n==0):
                return 1
            elif (n%2==0):
                return power(x*x,n//2)
            else:
                return x*power(x*x,(n-1)//2)
        res=power(x,abs(n))
        return float(res) if n>=0 else 1/res

        
        # if n == 0:
        #     return 1
        # half_pow = pow(x,n//2)
        # if n%2 :
        #     return (half_pow * half_pow * x )
        # return (half_pow*half_pow)


        # def function(base=x, exponent=abs(n)):
        #     if exponent == 0:
        #         return 1
        #     elif exponent % 2 == 0:
        #         return function(base * base, exponent // 2)
        #     else:
        #         return base * function(base * base, (exponent - 1) // 2)

        # f = function()
        
        # return float(f) if n >= 0 else 1/f

