# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def fun(root,node):
#             newnode = TreeNode(node)
#             if root.val > node:
#                 root.left = newnode
#             else:
#                 root.right = newnode
#         mid=len(nums)//2
#         root=TreeNode(nums[mid])
#         for i in range(1,len(nums)):
#             fun(root,nums[i])
#         return root
            
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(root, node):
            if root is None:
                return TreeNode(node)
            if node < root.val:
                root.left = fun(root.left, node)
            else:
                root.right = fun(root.right, node)
            return root

        def constructBST(nums, left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = constructBST(nums, left, mid - 1)
            root.right = constructBST(nums, mid + 1, right)

            return root

        if not nums:
            return None

        return constructBST(nums, 0, len(nums) - 1)


            
