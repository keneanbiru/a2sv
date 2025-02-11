class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        par = list(part)
        stack = []
        for i  in s:
            stack.append(i)
            if len(stack) >= len(part):
                if stack[len(stack) - len(part) : ] == par:
                    for i in range(len(part)):
                        stack.pop()
        return "".join(stack)
                    
        