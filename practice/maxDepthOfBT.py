# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # APPROACH 1 : RECURSIVE DFS
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        # APPROACH 2 : BFS
        # if not root:
        #     return 0
        
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        
        # return level
        
        # APPROACH 3 : ITERATIVE DFS
        if not root:
            return 0
        
        stk = [[root, 1]]
        res = 1
        while stk:
            node, depth = stk.pop()
            
            if node:
                res = max(res, depth)
                stk.append([node.left, depth + 1])
                stk.append([node.right, depth + 1])
                
        return res