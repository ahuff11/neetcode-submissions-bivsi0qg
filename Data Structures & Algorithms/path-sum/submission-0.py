# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        count = 0

        def leafpath(root, count):

            if not root:
                return False
            count += root.val

            if not root.left and not root.right and count == targetSum:
                return True
            if leafpath(root.left, count):
                return True
            if leafpath(root.right, count):
                return True
            
            count -= root.val
            return False
        
        return leafpath(root, count)