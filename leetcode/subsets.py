class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        bucket = []
        def backtrack (i):
          
            ans.add(tuple(bucket[:]))
            for j in range(i,n):
                bucket.append(nums[j])
                backtrack(j+1)
                bucket.pop()

        backtrack(0)
        return list(ans)


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       #TLE
       
        # def backtrack(bucket):
        #     if len(bucket) < n :
        #         bucket.sort()
        #         if tuple(bucket) not in ans:
        #             ans.add(tuple(bucket[:]))
        #     if len(bucket) == n:
        #         ans.add(tuple(bucket[:]))
        #         return 
        #     for i in nums:
        #         # bucket.sort()
        #         if i not in bucket:
        #             bucket.append(i)
        #             backtrack(bucket)
        #             bucket.pop()
        # backtrack(bucket)
        # return ans


        