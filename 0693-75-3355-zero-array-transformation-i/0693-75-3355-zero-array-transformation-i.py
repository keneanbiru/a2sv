class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n, m=len(nums), len(queries)
        f=[0]*(n+1)
        for s, e in queries:
            f[s]+=1
            f[e+1]-=1
        op=0
        for i, x in enumerate(nums):
            op+=f[i]
            if x>op: return False
        return True

        