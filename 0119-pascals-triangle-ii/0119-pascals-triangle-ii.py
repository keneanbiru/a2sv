class Solution:
    def getRow(self, row: int) -> List[int]:
        def fun(num):
            if num == 0:
                return [1]
            
            prev = fun(num - 1)

            cur = [1]

            for i in range(len(prev)-1):
                cur.append(prev[i]+prev[i+1])
            
            cur.append(1)
            return cur
        return fun(row)













        if row == 0:
            return [1]
        
        prev = self.getRow(row - 1)
        cur = [1]
        for i in range(1,len(prev)):
            cur.append(prev[i-1] + prev[i])
        cur.append(1)
        return cur
        