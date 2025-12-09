class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # cnt = Counter(nums)
        MOD = 10**9 + 7
        ans = 0
        right =  Counter(nums)
        left = defaultdict(int)

        for i in nums:
            right[i] -=1
            if right[i] <=0:
                del right[i]
            if i*2 in right and i*2 in left:
                ans += (left[i*2] * right[i*2]) % MOD
            left[i]+=1
            # print(right,left,ans)
        return ans%MOD


        