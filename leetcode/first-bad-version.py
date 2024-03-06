# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n+1
        while left+1 < right:
            mid = (left+right)//2
            if (isBadVersion(mid)):
                right = mid
            else:
                left = mid
        return right

        
        
        
        
        # mid = math.ceil(n/2)
        # print(mid)
        # while not isBadVersion(mid-1):
        #     if (isBadVersion(mid)):
        #         mid = mid//2
        #     mid=(mid + n)//2
        