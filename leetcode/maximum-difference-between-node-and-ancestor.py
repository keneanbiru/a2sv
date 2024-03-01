# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # maxi=root.val
        # mini=root.val
        # def helper(root,maxi,mini):
        #     if not root.left and not root.right:
        #         return maxi-mini
        #     if (mini>root.left.val ):
        #         mini=root.left.val
        #     if (maxi<root.left.val):
        #         maxi=root.left.val
        #     return helper(root.left,maxi,mini)
        #     max_left=maxi
        #     min_left=mini
        #     if (maxi < root.right):
        #         maxi = root.right.val
        #     if (mini>root.right.val):
        #         mini=root.right.val
        #     return helper(root.right,maxi,mini)
        #     max_right=maxi
        #     mini_right=mini
        #     return max(max_left-mini_left,maxi_right-mini_right)
        
        # res=(helper(root,maxi,mini))
        # print(res)
        # return res        

        def helper(root, maxi, mini):
            if not root:
                return 0
            
            if root.val > maxi:
                maxi = root.val
            if root.val < mini:
                mini = root.val
                
            left_diff = helper(root.left, maxi, mini)
            right_diff = helper(root.right, maxi, mini)
            
            return max(maxi - mini, left_diff, right_diff)
        
        return helper(root, root.val, root.val)


