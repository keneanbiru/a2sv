class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        s = [[] for _ in range(n)]
        for l, r in queries:
            s[l].append(r)

        av = []   
        ac = []  
        ch = 0
        for i in range(n):
            for r in s[i]:
                heapq.heappush(av, -r)

            while ac and ac[0] < i:
                heapq.heappop(ac)

            need = nums[i] - len(ac)
            for _ in range(need):
                while av and -av[0] < i:
                    heapq.heappop(av)
                if not av:
                    return -1
                r = -heapq.heappop(av)
                heapq.heappush(ac, r)
                ch += 1
        return q - ch