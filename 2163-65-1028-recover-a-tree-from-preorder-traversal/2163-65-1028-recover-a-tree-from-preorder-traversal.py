# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        mapp = []
        i = 0
        while i < len(s):
            depth = 0
            while i < len(s) and s[i] == '-':
                depth += 1
                i += 1
            num = 0
            while i < len(s) and s[i] != '-':
                num = num * 10 + int(s[i])
                i += 1
            mapp.append((depth, num))

        stack = []
        root = None
        
        for depth, nodeVal in mapp:
            node = TreeNode(nodeVal)
            
            while stack and stack[-1][0] >= depth:
                stack.pop()
            
            if stack:
                parent = stack[-1][1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            else:
                root = node
            
            stack.append((depth, node))
        
        return root