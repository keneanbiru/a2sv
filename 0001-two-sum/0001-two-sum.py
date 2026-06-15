class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = dict()

        for i,num in enumerate(nums):
            val = target - num
            if val not in dict1:
                dict1[num] = i
            else:
                return [dict1[val] ,i]