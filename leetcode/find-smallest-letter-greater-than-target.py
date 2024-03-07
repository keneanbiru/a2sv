class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l + r)//2
            if letters[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        
        return letters[l % len(letters)]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # mini = min(letters)
        # maxi = max(letters)
        # if target < mini:
        #     return mini
        # if target > maxi :
        #     return mini 
        # left = ord(mini)
        # right = ord(maxi)

        # while left < right:
        #     mid = (left + right) //2
        #     # print(mid)
        #     if chr(mid) < target:
        #         left = mid+1
        #     elif chr(mid) > target:
        #         right = mid-1
        #     elif chr(mid) == target:
        #         print(chr(left))
        #         print(chr(right))
        #         return chr(mid)
        #     else:
        #         print(chr(left))
        #         print(chr(right))
        #         return chr(right)


