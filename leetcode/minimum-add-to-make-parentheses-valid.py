class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if (i=='('):
                stack.append(i)
            else:
                if  stack and stack[-1]=="(":
                    print(stack[-1])
                    stack.pop()

                else:
                    stack.append(i)
        print(stack)
        return len(stack)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # opened,closed=0,0
        # n=len(s)
        # for i in s:
        #     if i=='(':
        #         opened+=1
        #         print("o",opened)
        #     else:
        #         closed+=1
        #         print(closed)
        # if(opened==closed):
        #     return 0
        
            