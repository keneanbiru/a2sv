class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list=path.split('/')
        print(path_list)
        stack=[]
        for i in path_list:
            if(i=="..") and stack :
                stack.pop()
            elif (i!="." and i!="" and i!=".."): 
                stack.append(i)
        res="/"+"/".join(stack)
        return res

