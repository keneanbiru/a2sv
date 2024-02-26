class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # def fun (x):
        #         if(x==1):
        #             return 5
        #         elif (x%2==0):
                    
        #             return (4*fun(x-1))
                   
        #         else:
                    
        #             return (5*fun(x-1))
      


        # res=(fun(n)%(10**9+7))
        # return res
        
        # ans = 1
        # x = 20
        # temp = n//2
        # while temp!=0:
        #     if temp&1!=0:
        #         ans*=x
        #     x*=x
        #     temp>>=1
        
        if(n==1):
            return 5
        
        elif (n%2==0):
            n=n//2
            return (pow(20,n,10**9+7))
        else:
            n=n//2
            return (pow(20,n,10**9+7)*5)%(10**9+7)
            
        # def fun (x):
        #         if(x==1):
        #             return 5
        #         elif (x%2==0):
                    
        #             return (4*fun(x-1))
                   
        #         else:
                    
        #             return (5*fun(x-1))
        
        # res=fun(n)%(10**9+7)
        # return res