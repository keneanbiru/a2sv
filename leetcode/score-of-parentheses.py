class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        
        for i in s:
            
            if i == "(":
                
                stack.append(0)
                
               
            else :
                val=max(2*stack.pop(),1)
                stack[-1]+=val
        return stack.pop()
       
       
       
        # stack = []
        # count = 0
        # _sum = 0
        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     if i == ")":
        #         if stack and stack[-1] == "(":
        #             stack.pop()
        #             count += 1
        #             _sum += 2 ** (count - 1)
        #             count = 0
        #         else:
        #             stack.append(i)
        # return _sum

            