# Binary Trees
print("BINARY TREES")
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

# Initializing Binary Tree 
#       1
#   2       3
# 4   5  10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
B.left = D
B.right = E
A.right = C
C.left = F

# print(A)

print("DEPTH FIRST SEARCH")
# DEPTH FIRST SEARCH TECHNIQUE
# Recursive Pre Order Traversal (DFS), Time: O(n), Space: O(n)
# Pre Order Traversal Pseudo Code: Node, Left, Right
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left) 
    pre_order(node.right)
    
print("Pre-order Traversal:")
pre_order(A)


# Recursive In Order Traversal (DFS), Time: O(n), Space: O(n)
# In Order Traversal Pseudo Code: Left, Node, Right
def in_order(node):
    if not node:
        return
    
    in_order(node.left) 
    print(node)
    in_order(node.right)
    
print("In-order Traversal:")
in_order(A)


# Recursive Post Order Traversal (DFS), Time: O(n), Space: O(n)
# Post Order Traversal Pseudo Code: Left, Right, Node
def post_order(node):
    if not node:
        return
    
    post_order(node.left) 
    post_order(node.right)
    print(node)
    
print("Post-order Traversal:")
post_order(A)

# Iterative Pre Order Traversal (DFS), Time: O(n), Space: O(n)
# Iterative meaning not using recursion but using stack
def iter_pre_order(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        
print("Iterative Pre-order Traversal:")
iter_pre_order(A)

print("BREATH FIRST SEARCH")
# BREATH FIRST SEARCH
# Level Order Traversal (BFS), Time: O(n), Space: O(n)
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        
print("Level Order Traversal")
level_order(A)


# Check if a value exists using DFS, Time: O(n), Space: O(n)
print("Searching through a binary tree")
def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

print(search(A, 4))

print("-----------------------------------------------------")
# Binary Search Trees
print("BINARY SEARCH TREES")

#       5
#   1       8
#-1   3   7   9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

# print(A2)

# In-order traversal is same for both BT and BST
print("In Order Traversal for Binary Search Trees")
in_order(A2)


# Check if an item exists in a binary search tree
def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)
    
print("Searching through a binary search tree")
print(search_bst(A2, 9))