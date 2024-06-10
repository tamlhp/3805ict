"""
Function SplayTopDown(root, key)
    Create LeftTreeMax and RightTreeMin temporary nodes
    while true
        if key < current node's key
            if left child is nil, break
            if key < left child's key, rotate right
            Link current node to RightTreeMin
            Move to left child
        else
            if right child is nil, break
            if key > right child's key, rotate left
            Link current node to LeftTreeMax
            Move to right child
        if current node is nil, break
    Reassemble tree:
        LeftTreeMax's right = current node's left
        RightTreeMin's left = current node's right
        current node's left = LeftTreeMax's right
        current node's right = RightTreeMin's left
        root = current node

Function InsertTopDown(key)
    SplayTopDown(root, key)
    if root is not key
        Create new node with key
        if root is nil, new node becomes root
        else, insert new node as root, adjust children
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

# Top-down splay function
def splay_top_down(node, key):
    global root
    if node is None:
        return None

    # Create dummy nodes for the sake of simplicity in handling edges
    leftTreeMax = leftTemp = Node(None)  # Temporary node for the left subtree
    rightTreeMin = rightTemp = Node(None)  # Temporary node for the right subtree

    while True:
        if key < node.key:
            if node.left is None:
                break
            if key < node.left.key:
                # Rotate right
                temp = node.left
                node.left = temp.right
                temp.right = node
                node = temp
                if node.left is None:
                    break
            # Link right
            rightTemp.left = node
            rightTemp = node
            node = node.left
        else:
            if node.right is None:
                break
            if key > node.right.key:
                # Rotate left
                temp = node.right
                node.right = temp.left
                temp.left = node
                node = temp
                if node.right is None:
                    break
            # Link left
            leftTemp.right = node
            leftTemp = node
            node = node.right

        if node is None:
            break

    # Assemble
    leftTemp.right = node.left
    rightTemp.left = node.right
    node.left = leftTreeMax.right
    node.right = rightTreeMin.left
    root = node

# Modified insert function for top-down splaying
def insert_top_down(key):
    global root
    # Splay the tree for key and then insert if it doesn't exist
    splay_top_down(root, key)
    if root and root.key == key:  # If the key is already in the tree, it's now at the root
        return

    new_node = Node(key)
    if root is None:
        root = new_node
        return

    if key < root.key:
        new_node.left = root.left
        new_node.right = root
        root.left = None
        root = new_node
    else:
        new_node.right = root.right
        new_node.left = root
        root.right = None
        root = new_node


# Construct the initial tree from the provided image
root = Node(100)
root.left = Node(50, parent=root)
root.left.right = Node(60, parent=root.left) 
root.left.left = Node(40, parent=root.left)
root.left.left.left = Node(30, parent=root.left.left)
root.right = Node(150, parent=root)
root.right.right = Node(200, parent=root.right)

# Using the same initial tree structure
# Now insert key 180 with top-down splaying
insert_top_down(180)

# Print the tree after top-down splay inserting 180
print("Tree after inserting 180 with top-down splaying:")
print_tree(root)

