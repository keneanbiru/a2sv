# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum1 = 0
        def fun(root):
            nonlocal sum1
            if not root:
                return 0
            if (low <= root.val <= high):
                sum1 += root.val
            fun(root.left)
            fun(root.right)
            return sum1
        return fun(root)
        
        