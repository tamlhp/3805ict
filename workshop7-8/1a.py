"""
Bottom-Up Splaying (for part a):
When you insert a new node into a splay tree, you first insert it as you would in a regular BST. After insertion, you perform splay operations to move the new node to the root of the tree. If the parent of the new node is not the root, you perform either a zig-zig, zig-zag, or zig rotation depending on the configuration.

Zig: Single rotation (the inserted node has a grandparent and is a right child followed by a left child or vice versa).
Zig-Zig: Double rotation (the inserted node and its parent are both right children or both left children).
Zig-Zag: Double rotation but in the opposite direction (the inserted node is a right child and its parent is a left child or vice versa).

function InsertAndSplayBottomUp(tree, key):
    InsertNode(tree, key)
    node = FindNode(tree, key)
    while node is not root:
        if node.parent is root:
            Zig(node)
        else if (node is left child and node.parent is left child) or (node is right child and node.parent is right child):
            ZigZig(node)
        else:
            ZigZag(node)
"""

class Node:
    def __init__(self, key, color='B', left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

# Helper function to print the tree
def print_tree(node, indent="", last="up"):
    if node:
        print(f"{indent} {last}-- {node.key}({node.color})")
        indent += "   " if last == "up" else " |  "
        print_tree(node.left, indent, "left")
        print_tree(node.right, indent, "right")

# Function to perform a left tree rotation
def rotate_left(x):
    global root
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if not x.parent:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return y  # Return the new root if necessary

# Function to perform a right tree rotation
def rotate_right(y):
    global root
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x
    return x  # Return the new root if necessary

# Function to splay a node (bottom-up splaying)
def splay(node):
    global root
    while node.parent:
        if not node.parent.parent:
            if node.parent.left == node:
                root = rotate_right(node.parent)
            else:
                root = rotate_left(node.parent)
        elif node.parent.left == node and node.parent.parent.left == node.parent:
            rotate_right(node.parent.parent)
            root = rotate_right(node.parent)
        elif node.parent.right == node and node.parent.parent.right == node.parent:
            rotate_left(node.parent.parent)
            root = rotate_left(node.parent)
        elif node.parent.left == node and node.parent.parent.right == node.parent:
            rotate_right(node.parent)
            root = rotate_left(node.parent.parent)
        elif node.parent.right == node and node.parent.parent.left == node.parent:
            rotate_left(node.parent)
            root = rotate_right(node.parent.parent)

# Function to insert a node and splay the tree
def insert(key):
    global root
    if root is None:
        root = Node(key)
        return
    node = root
    while True:
        if key < node.key:
            if node.left:
                node = node.left
            else:
                node.left = Node(key, parent=node)
                node = node.left
                break
        else:
            if node.right:
                node = node.right
            else:
                node.right = Node(key, parent=node)
                node = node.right
                break
    splay(node)

# Construct the initial tree from the provided image
root = Node(100)
root.left = Node(50, parent=root)
root.left.right = Node(60, parent=root.left) 
root.left.left = Node(40, parent=root.left)
root.left.left.left = Node(30, parent=root.left.left)
root.right = Node(150, parent=root)
root.right.right = Node(200, parent=root.right)

# Insert key 10 and splay the tree
insert(10)

# Print the tree after splaying
print("Tree after inserting 10 and splaying:")
print_tree(root)

