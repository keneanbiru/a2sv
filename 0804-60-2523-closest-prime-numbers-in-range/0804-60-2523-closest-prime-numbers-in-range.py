class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def seive(x):
            arr = [True] * (x+1)
            arr[0],arr[1]  = False,False
            i =2
            while i*i <= x:
                
                if arr[i]:
                   for j in range(i*i,x+1,i):
                        arr[j]=False
                i+=1
           
            res = []
            
            for i in range(left,x+1):
                if arr[i]==True:
                    res.append(i)
            return res
        arr2 = seive (right)
        mini = float("inf")
        ans = []
        for i in range(len(seive (right))-1):
            temp = mini
            mini = min (mini,arr2[i+1]-arr2[i])
            if temp!=mini:
                ans = [arr2[i],arr2[i+1]]
        if ans ==[]:
            return [-1,-1]
        else:
            return ans

            

        