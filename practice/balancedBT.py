# MY OWN SOLUTION THAT PASSED 8 CASES
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         self.leftS = 0
#         self.rightS = 0
#         self.balance = True

#         def dfs(curr):
#             if not curr:
#                 return 0
            
#             self.leftS = left = dfs(curr.left)
#             if abs(self.leftS - self.rightS) > 1:
#                 self.balance = False
#             self.rightS = right = dfs(curr.right)

#             return 1 + max(left, right)
        
#         dfs(root)
#         if self.balance == False:
#             return False
#         else:
#             return True
        
# ACTUAL CORRECT AND OPTIMIZED SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]