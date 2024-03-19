class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        mini = float("inf")
        for i in range(len(nums)):
            mid = i
            l = mid +1
            r = n-1
            while l< r:
                mini_o = mini
                cur = nums[mid]+nums[l]+nums[r]
                mini = min(abs(cur-target),mini)
                if mini!=mini_o:
                    ans = cur
                if cur<target:
                    l+=1
                elif cur>target:
                    r-=1
                else:
                    return cur
        return ans
