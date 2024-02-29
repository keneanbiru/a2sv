# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict1 = defaultdict(list)
        level = 0
        def helper(level,root):
            if root:
                dict1[level].append(root.val)
                level+=1
                helper(level,root.left)
                helper(level,root.right)
        helper(level,root)
        ans=[]
        for i in dict1:
            if i%2==0:
                ans.append(dict1[i])
            else:
                dict1[i].reverse()
                ans.append(dict1[i])
        return ans

        