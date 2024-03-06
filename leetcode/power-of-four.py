class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        def fun(n):
            # print(n)
            if n == 4.0:
                return True
          
            if n < 4.0:
                return False
            
            return fun(n/4)
        return fun (n)