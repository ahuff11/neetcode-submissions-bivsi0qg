# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs each level
        # if we are on the right side, check the rightmost node, if there isn't append the left
        # if we have appended something on this level we can skip to the next level
        # check if there is a right node, if there is append it

        ans = []
        queue = deque()

        if root:
            queue.append(root)


        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level.pop())
            
        return ans