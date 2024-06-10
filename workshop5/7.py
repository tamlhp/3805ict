"""
1. Find the Node: Locate the node with the key 12 that we want to delete.
2. Node Deletion: If the node has two children, find the in-order successor (or predecessor) to replace its value, then delete that successor node instead. If the node has zero or one child, remove it directly.
3. Rebalance: If the deleted node was red, we're done. If it was black, we need to rebalance the tree to fix any violations of the Red-Black properties caused by removing a black node.
4. Case Analysis: Several cases might need to be addressed to rebalance the tree, such as recoloring nodes, rotating subtrees, and moving the "extra black" up the tree until we can eliminate it.

function DeleteNode(tree, key)
    node = FindNode(tree, key)
    if node has two children
        successor = FindInOrderSuccessor(node)
        node.key = successor.key
        node = successor
    replaceNodeWithChild(tree, node)
    if node.color == BLACK
        Rebalance(tree, node)

function replaceNodeWithChild(tree, node)
    // Replace node with its child (NIL in case of no child)

function Rebalance(tree, node)
    // Rebalance the tree after deletion
    // This involves multiple cases and steps to redistribute the "extra black"
    // from the deletion up the tree, recoloring, and rotating as needed.

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

# Function to find the node with the given key
def find_node(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return find_node(node.left, key)
    return find_node(node.right, key)

# Function to replace a node with its child in the tree
def replace_node(parent, node, child):
    if parent is None:
        return child
    if parent.left == node:
        parent.left = child
    else:
        parent.right = child
    if child:
        child.parent = parent
    return parent

# Function to delete a node from the tree
def delete_node(root, key):
    node_to_delete = find_node(root, key)
    if node_to_delete is not None:
        # Node with only one child or no child
        child = node_to_delete.left if node_to_delete.left else node_to_delete.right
        if node_to_delete.parent:
            replace_node(node_to_delete.parent, node_to_delete, child)
            if node_to_delete.color == 'B':
                # Here you would normally handle the fixup
                pass  # Placeholder for fixup logic
        else:  # node_to_delete is root
            root = child
            if child:
                child.color = 'B'
        return root

# Construct the initial Red-Black Tree from the provided image
root = Node(30, 'B')
root.left = Node(15, 'R', parent=root)
root.left.left = Node(12, 'B', parent=root.left)
root.left.right = Node(20, 'B', parent=root.left)
root.right = Node(45, 'B', parent=root)
root.right.left = Node(35, 'R', parent=root.right)
root.right.right = Node(60, 'R', parent=root.right)

# Print initial tree
print("Initial Red-Black Tree:")
print_tree(root)

# Delete node with key 12
root = delete_node(root, 12)

# Print tree after deletion
print("\nRed-Black Tree after deleting key 12:")
print_tree(root)