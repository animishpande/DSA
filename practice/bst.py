# BINARY TREES IMPLEMENTATION
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
# INITIALIZING THE BINARY TREE
#           1
#       2          3
#   4      5   10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# DEPTH FIRST SEARCH
print("DEPTH FIRST SEARCH")
def pre_order_traversal(node):
    if node is None:
        return
    
    print(node)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

print("Pre-Order Traversal")
pre_order_traversal(A)

def in_order_traversal(node):
    if node is None:
        return
    
    in_order_traversal(node.left)
    print(node)
    in_order_traversal(node.right)
    
print("In-Order Traversal")
in_order_traversal(A)

def post_order_traversal(node):
    if node is None:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node)

print("Post-Order Traversal")
post_order_traversal(A)

def iterative_pre_order(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        
print("Iterative pre-order traversal without recursion (using stack)")
iterative_pre_order(A)

# BREADTH FIRST SEARCH
print("BREADTH FIRST SEARCH")
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

print("Searching for a value in Binary Trees")
def search_binary(node, target):
    if node is None:
        return False
    
    if node.data == target:
        return True
    
    return search_binary(node.left, target) or search_binary(node.right, target)

val = search_binary(A, 10)
print(f"Is 10 in {A}? -> {val}")


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
in_order_traversal(A2)

print("Searching for a value in Binary Search Trees")
def search_BST(node, target):
    if node is None:
        return False
    
    if node.data == target:
        return True
    
    if target < node.data: return search_BST(node.left, target)
    else: return search_BST(node.right, target)
    
print(search_BST(A2, 9))