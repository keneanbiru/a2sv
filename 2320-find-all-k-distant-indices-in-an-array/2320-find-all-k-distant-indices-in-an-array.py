class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = set()
        for i in range(n):
            if nums[i] == key:
                cnt = k
                ans.add(i)
                while cnt:
                    if i - cnt >= 0 :
                        ans.add(i-cnt)
                    if cnt+i < n:
                        ans.add(cnt+i)
                    cnt-=1
        return(sorted(list(ans)))
                    

