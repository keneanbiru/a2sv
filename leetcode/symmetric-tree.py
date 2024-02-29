# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root1,root2):
            if not root1 and  not root2:
               return True
            if root1 and root2 and(root1.val!=root2.val):
                return False
            if root1 and root2:
                return helper(root1.left,root2.right) and helper(root1.right,root2.left)    
            return False
        return helper(root.right,root.left)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # val1=root.right.val 
        # # val2=root.left.val
        # # list1.append(val1)
        # # list2.append(val2)
        # root.right=self.isSymmetric(root.right)
        # val1=root.val
        # list1.append(val1)
        # root.left=self.isSymmetric(root.left) 
        # val2=root.val
        # list2.append(val2)
        # print(list1 ,list2)
        # if (list1!=list2):
        #     return False
        # else:
        #     return True