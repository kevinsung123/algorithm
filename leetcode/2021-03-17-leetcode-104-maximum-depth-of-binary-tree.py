# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        if not root:
            return 0
        q.append(root)
        maxdepth = 0
        while q:
            maxdepth += 1
            level_len = len(q)
        
            for _ in range(level_len):
                node = q.popleft()
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxdepth
if __name__=='__main__':

