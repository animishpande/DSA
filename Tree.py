print("TREE DATA STRUCTURE IN PYTHON")
# A TREE DATA STRUCTURE IS A NON-LINEAR DATA STRUCTURE CONSISTING OF NODES CONNECTED BY EDGES.
# IT COMPRISES OF A ROOT NODE WHICH SERVES AS A STARTING POINT AND EACH NODE CAN HAVE ONE OR ZERO CHILDREN NODES

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
#       1
#   2       4
#               8
        
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(4)
child3 = TreeNode(8)

root.add_child(child1)
root.add_child(child2)
child2.add_child(child3)


# SEARCHING OPERATIONS IN TREES
# DEPTH FIRST SEARCH
def depth_first_search(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    for child in node.children:
        if depth_first_search(child, target):
            return True
    return False

# PRE-ORDER
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    for child in node.children:
        pre_order_traversal(child)
        
pre_order_traversal(root)
search_data = depth_first_search(root, 2)
print(search_data)

# INSERTING A NODE IN THE TREE
def insert_node(root, node):
    if root is None:
        root = node
    else:
        root.add_child(node)

child4 = TreeNode(16)        
insert_node(child3, child4)

# DELETING A NODE FROM THE TREE
def delete_node(root, target):
    if root is None:
        return None
    root.children = [child for child in root.children if child.data != target]
    for child in root.children:
        delete_node(child, target)

delete_node(child3, 16)
        
# CALCULATING THE HEIGHT OF THE TREE
def tree_height(node):
    if node is None:
        return 0
    if not node.children:
        return 1
    return 1 + max(tree_height(child) for child in node.children)

height = tree_height(root)
print(f"Tree Height from Root -> {height}")

print("----------------------------------------------------------------------------------------------------------")

# BINARY TREES
# A BINARY TREE IS A TREE DATA STRUCTURE WHERE EACH NODE HAS ATMOST A LEFT AND A RIGHT CHILD.
class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = BinaryNode(1)
a = BinaryNode(2)
b = BinaryNode(3)
c = BinaryNode(4)
d = BinaryNode(5)
e = BinaryNode(6)
f = BinaryNode(7)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f

       
    