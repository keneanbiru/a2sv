class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans = set()
        bucket = []
        def backtrack(i):
            print(sorted (bucket))
            if tuple(sorted(bucket)) not in ans:
                ans.add(tuple(sorted(bucket[:])))
                
            for j in range(i,n):
                bucket.append(nums[j])
                print("appended",nums[j])
                backtrack(j+1)
                print("poped",bucket.pop())
        backtrack(0)
        return ans
         
        