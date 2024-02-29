# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print(type(p))
        # if root.val==p.val: 
        #     return p.val
        # if root.val==q.val:
        #     return q.val
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor (root.right,p,q)
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif (p.val>root.val and q.val<root.val) or (q.val>root.val and p.val<root.val):
            return root
        elif p.val==root.val:
            return p
        elif q.val==root.val:
            return q

        

        