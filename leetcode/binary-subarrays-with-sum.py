class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = prefix = 0
        counter = defaultdict(int)
        counter[0] = 1
        # print(counter)
        for num in nums:
            prefix += num
            if prefix - goal in counter:
                ans += counter[prefix - goal]

            if prefix not in counter:
                counter[prefix] = 1

            else:
                counter[prefix] += 1
            # print(counter)

        return ans