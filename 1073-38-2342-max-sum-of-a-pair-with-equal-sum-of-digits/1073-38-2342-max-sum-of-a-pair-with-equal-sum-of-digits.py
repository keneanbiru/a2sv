class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapp = defaultdict(list)

        for i in nums:
            summ = sum(map(int, str(i)))
            mapp[summ].append(i)
        ans = -1
        for key,val in mapp.items():
            if len(val) >1:
                val.sort()
                ans = max(ans , val[-1] + val[-2])
        return ans


