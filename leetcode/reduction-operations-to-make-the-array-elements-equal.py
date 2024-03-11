class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        setted = list(set(nums))
        setted.sort()
        dict1 = {}
        ans = 0
        for i in range(len(setted)):
            dict1[setted[i]] = i
        # print(dict1)
        for i in nums:
            ans+= dict1[i]
        return ans
