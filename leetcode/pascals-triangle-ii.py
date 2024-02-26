class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        list1=[]
        def fact (x):
            if (x==1 or x==0):
                return 1
            return (x*fact(x-1))
        for i in range(rowIndex+1):
            
            res=fact(rowIndex)//(fact(rowIndex-i)* fact(i))  
            list1.append(res)
        
        return list1      