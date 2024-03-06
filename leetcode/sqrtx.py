class Solution:
    def mySqrt(self, x: int) -> int:
        left = -1
        right = x+1
        
        while left+1 < right:
            mid = (left+right)//2
            if mid*mid < x:
                left =mid+1
            elif mid*mid > x:
                right = mid-1
            else:
                return mid
        print(left)
        if  left*left > x:
            return left-1
        elif (left+1)*(left+1) <= x:
            return left+1
        return left
       
        

            
        