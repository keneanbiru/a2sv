class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set() 
        bucket = [] 
        candidates.sort() 
 
        def backtrack(i): 
 
            if sum(bucket) > target: 
                return  
   
            if sum(bucket) == target: 
                 
                ans.add(tuple(bucket[:])) 
                return  
            hold = None 
            for j in range(i, len(candidates)): 
                 
                if candidates[j] != hold: 
                    bucket.append(candidates[j]) 
                    backtrack(j+1) 
                    hold = bucket.pop() 
 
 
        backtrack(0) 
        out = [] 
 
        for i in ans: 
            out.append(list(i)) 
 
        return ans