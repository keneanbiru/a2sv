class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        exp=set(["+", "-", "*", "/"])
        for i in tokens:
            if i in exp:
                x=stack.pop()
                y=stack.pop()
                if i == "+":
                    res=y + x
                    stack.append(res)
                elif i == "-":
                    res=y - x
                    stack.append(res)
                    
                elif i == "*":
                    res=y * x
                    stack.append(res)
                    
                elif (i=="/"):
                    
                    res=y / x
                    if res<0:
                        res=math.ceil(res)
                    stack.append(int(res))
                    
            else:
                i=int(i)
                stack.append(i)
                
        return stack[-1]
