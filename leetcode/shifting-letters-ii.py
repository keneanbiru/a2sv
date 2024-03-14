class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr1 = []
        res = []
        res2 = []
        arr2 = [0]*(len(s)+1)
        def ps( nums):
            total = 0
            for i in range(len(nums)):
                total += nums[i]
                nums[i] = total
            return nums
        
        for i in range(len(shifts)) :
            if shifts[i][2]==0:
                arr2[shifts[i][0]] -=1
                arr2[shifts[i][1]+1] +=1
            else:
                arr2[shifts[i][0]] +=1
                arr2[shifts[i][1]+1]-=1
        res = ps(arr2)
        # print(arr2)
        arr2.pop()
        for i in s:
            arr1.append(ord(i) - ord('a'))
        for i in range(len(s)):
            res2.append(chr((arr1[i] + arr2[i])%26 +97))
        # print(res2)

        return "".join(res2)
