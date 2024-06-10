"""
1. Insert Like a BST: Insert the new node 50 as you would in a regular binary search tree. This node will be red.
2. Rebalance: Check for violations of the Red-Black Tree properties and fix them:
If the parent of the new node is black, you're done.
If the parent is red, you may need to rotate and/or recolor nodes.
3. Case Analysis: The steps to fix the tree depend on the colors of the surrounding nodes (the parent, uncle, and grandparent of the new node).
Case 1: The uncle is red. Recolor the parent and uncle black, and the grandparent red. Then, move to the grandparent and check again.
Case 2: The uncle is black, and the new node is a right child. Perform a left rotation to switch the new node and its parent, then handle as case 3.
Case 3: The uncle is black, and the new node is a left child. Recolor and perform a right rotation at the grandparent.
4. Final Touch: Ensure the root is black.

function InsertNode(tree, key)
    newNode = CreateNode(key, RED)
    InsertBST(tree, newNode)  // Regular BST insertion
    Rebalance(tree, newNode)  // Fix the tree to maintain red-black properties

function Rebalance(tree, node)
    while node is not root and node.parent.color is RED
        if node.parent is left child of grandparent
            uncle = grandparent.right
            if uncle.color is RED
                // Case 1: Recolor
            else if node is right child of parent
                // Case 2: Rotate left at parent
            else
                // Case 3: Rotate right at grandparent
        // Mirror cases for when the node's parent is the right child
    tree.root.color = BLACK

"""


class Node:
    def __init__(self, key, color="red", left=None, right=None, parent=None):
        self.key = key
        self.color = color  # All new nodes in a Red-Black tree are red by default
        self.left = left
        self.right = right
        self.parent = parent

def insert(root, key):
    if not root:
        return Node(key, "black")  # New root is always black
    else:
        if key < root.key:
            if root.left:
                insert(root.left, key)
            else:
                root.left = Node(key, "red", parent=root)
        else:
            if root.right:
                insert(root.right, key)
            else:
                root.right = Node(key, "red", parent=root)
    return root

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(f"{root.key}({root.color})", end=" ")
    inorder_traversal(root.right)

# Creating the initial Red-Black tree from the image provided
root = Node(30, "black")
root.left = Node(15, "red", parent=root)
root.right = Node(45, "black", parent=root)
root.right.left = Node(35, "red", parent=root.right)
root.right.right = Node(60, "black", parent=root.right)
root.right.right.left = Node(55, "red", parent=root.right.right)

# Insert new key 50
insert(root, 50)

# In a real Red-Black Tree implementation, we would now need to balance the tree
# since we've added a new red node that could violate the properties of the tree.
# However, the balancing code (rotations, recoloring) is not included here.

# Print out the tree in-order to show the final result
print("In-order traversal of the Red-Black tree after inserting 50:")
inorder_traversal(root)
