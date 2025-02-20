class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = ["0" , "1"]
        n  = len(nums[0])
        def backtrack(cur):
            if len(cur) == n:
                p = "".join(cur)
                if p not in nums:
                    return p
                else:
                    return None
            for i in s:
                cur.append(i)
                res = backtrack(cur)
                if res:
                    return res
                cur.pop()
                
        return backtrack([])
            

        