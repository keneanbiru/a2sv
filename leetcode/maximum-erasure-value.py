class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
       
        indices = dict()
        l = 0
        cur = 0
        ans = 0

        for right, num in enumerate(nums):
            if num in indices and indices[num] >= l:
                while l <= indices[num]:
                    cur -= nums[l]
                    l += 1

            cur += num
            indices[num] = right
            ans = max(ans, cur)

        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # dict1 = defaultdict(list)
            # for i in range(len(nums)):
            #     dict1[nums[i]].append(i)
            # for i in range(len(nums)):
            #     if len(dict1[nums[i]]) == 1:
            #         res = len(nums) -i
            #     else:
                    

