class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        cnt = Counter([0])
        res = 0
        pre = 0
        for i in range(n):
            pre += 1 if nums[i] % modulo == k else 0
            res += cnt[(pre - k + modulo) % modulo]
            cnt[pre % modulo] += 1
        return res