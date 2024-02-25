class Solution:
    def isValid(self, s: str) -> bool:
        arr1=[]
        for i in s:
            
            if (i=='('  or i=='[' or i=='{'):
                arr1.append(i)
            elif (len(arr1)!=0):  
                if (i==')'):
                    
                    res=arr1[-1]
                    if (res!='('):
                        return False
                    else:
                        arr1.pop()
                elif (i=='}'):
                    res=arr1[-1]
                    if (res!='{'):
                        return False
                    else:
                        arr1.pop()
                else :
                    res=arr1[-1]
                    if (res!='['):
                        return False
                    else:
                        arr1.pop()
            else:
                return False
        return (len(arr1)==0)


            
                