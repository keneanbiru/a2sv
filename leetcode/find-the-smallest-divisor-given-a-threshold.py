class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        def fun(div):
            summ = 0
            for i in nums:
                summ += ceil(i/div)
            print(summ)
            return summ
        if (sum(nums) <= threshold):
            return 1

        left = 1
        right = max(nums)
        while left <= right:
            mid = (left+right)//2
            if (fun(mid) > threshold):
                left = mid + 1
            else:
                right = mid -1
        return left
     


