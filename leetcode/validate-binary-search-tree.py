# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_=[]
        def inorder(root):
            if not root :
                return
            inorder(root.left)
            inorder_.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len (inorder_)-1):
            if (inorder_[i]>=inorder_[i+1]):
                return False
        return True
























        #     if not root:
    #         return True
    #     if root.left and root.right:
    #         if (root.val>root.left.val   and root.val<root.right.val ):
    #             return self.isValidBST(root.left)
    #             return self.isValidBST(root.right)
    #     else:
    #         return False
    #     return False



    # in
        
 