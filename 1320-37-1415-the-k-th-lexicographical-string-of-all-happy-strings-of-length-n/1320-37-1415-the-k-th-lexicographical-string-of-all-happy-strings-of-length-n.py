class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        let = ["a","b","c"]
        ans = []
        def backtrack(cur,last):
            if len(cur) == n:
                ans.append("".join(map(str , cur)))
                return
            
            for i in let:
                if last != i:
                    cur.append(i)
                    backtrack(cur,i)
                    cur.pop()
            
        backtrack([],"")
        
        return ans[k-1] if k<=len(ans) else ""





