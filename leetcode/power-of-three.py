class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        def fun(n):
            print(n)
            if n == 3.0:
                return True
          
            if n < 3.0:
                return False
            
            return fun(n/3)
        return fun (n)