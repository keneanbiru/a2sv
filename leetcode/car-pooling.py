class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0]*1001
        prefix = 0
        for i in trips:
            
            ans[i[1]]+=i[0]
            ans[i[2]]-=i[0]
       
        for i in range(len(ans)):
            prefix += ans[i]
            
            ans[i] = prefix
        
        for i in ans:
            if i>capacity:
                return False
        return True