class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
'''
              1
        2           5
    3      4     6      7
'''
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(5)
D = TreeNode(3)
E = TreeNode(4)
F = TreeNode(6)
G = TreeNode(7)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

print("DEPTH FIRST SEARCH")
# Recursive Pre Order Traversal (DFS), Time: O(n), Space: O(n)
# Pre Order Traversal Pseudo Code: Node, Left, Right
print("Pre-Order Traversal -> Node, Left, Right")
def preOrderTraversal(node):
    if not node:
        return
    
    print(node)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

preOrderTraversal(A)

# Recursive In Order Traversal (DFS), Time: O(n), Space: O(n)
# In Order Traversal Pseudo Code: Left, Node, Right
print("In-Order Traversal -> Left, Node, Right")
def inOrderTraversal(node):
    if not node:
        return
    
    inOrderTraversal(node.left)
    print(node)
    inOrderTraversal(node.right)

inOrderTraversal(A)

# Recursive Post Order Traversal (DFS), Time: O(n), Space: O(n)
# Post Order Traversal Pseudo Code: Left, Right, Node
print("Post-Order Traversal -> Left, Right, Node")
def postOrderTraversal(node):
    if not node:
        return
    
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node)

postOrderTraversal(A)


# Iterative Pre Order Traversal (DFS), Time: O(n), Space: O(n)
# Iterative meaning without using recursion
# Iterative Pre Order Pseudo Code: Node, Right, Left
print("Iterative Pre Order Traversal -> Node, Right, Left")
def iterPreOrderTraversal(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

iterPreOrderTraversal(A)


print("BREADTH FIRST SEARCH")

# Level Order Traversal (BFS), Time: O(n), Space: O(n)
# Level Order Traversal Pseudo Code: Node, Left, Right
print("Level Order Traversal -> Node, Left, Right")
from collections import deque
def levelOrderTraversal(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

levelOrderTraversal(A)

# Searching for an element through a binary tree
print("Binary Search for searching through binary tree")
'''
Pseudo Code:
def search
if node == target:
    return node
else search(left node) or search(right node)
'''
def binarySearch(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return binarySearch(node.left, target) or binarySearch(node.right, target)

print(binarySearch(A, 10))