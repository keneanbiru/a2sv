# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict1 = defaultdict(int)
        def fun(root):
            nonlocal dict1
            if not root:
                return 
            dict1[root.val] +=1
            fun(root.left)
            fun(root.right)
        fun(root)
        maxi  = max(dict1.values())
        # print(maxi)
        ans = []
        for key ,value in dict1.items():
            if value == maxi:
                ans.append(key)
        return ans

        return []


