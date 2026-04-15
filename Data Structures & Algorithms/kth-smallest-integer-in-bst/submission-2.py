# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use nonlocal for the count and res or mutable counter
        # so we start counting once we start working our way back up the tree
        count = k
        res = root.val

        def dfs(node):
            nonlocal count, res
            if not node:
                return 
            
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res