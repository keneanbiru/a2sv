class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = prefix = 0
        count = defaultdict(int)
        count[0] = 1
        for num in nums:
            prefix +=num
            # print(prefix)
            mod = (prefix % k + k ) % k 
            if mod in count:
                ans += count[mod] 
            
            count[mod] += 1
        return ans