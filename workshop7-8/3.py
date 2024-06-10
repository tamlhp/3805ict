"""
A splay tree is a self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again. The basic idea is to move accessed items closer to the root of the tree using a process called splaying.

Here are the operations you asked about:

max(): Finds the maximum item in the tree, which will be the rightmost node. After finding it, the tree is splayed at this node, bringing it to the root.
insert(x): Inserts an item into the tree. If the item is not already in the tree, it is added at the correct location, and then the tree is splayed at this new node, bringing it to the root.
find(x): Searches for an item in the tree. If found, the tree is splayed at this node, bringing it to the root. If not found, the tree is splayed at the last accessed node.
remove(x): Removes an item from the tree. If the item is found, the tree is splayed at the parent of the removed node, then the two resulting subtrees are combined.

function splay(node)
    // Rotate node to root using rotations based on node's position (zig, zig-zig, zig-zag)

function max()
    // Find the rightmost node, then splay at this node

function insert(x)
    // Insert x into the tree according to binary search tree rules
    // Splay at the newly inserted node

function find(x)
    // Search for x in the tree
    // If found, splay at this node
    // If not found, splay at the last accessed node

function remove(x)
    // Find and remove x from the tree
    // Splay at the parent of the removed node
    // Combine the two resulting subtrees

"""
class Node:
    """A Node of a Splay Tree, which contains a key and pointers to its left and right children."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    """Implements a Splay Tree with operations like insert, find, and splay."""
    def __init__(self, root=None):
        self.root = root

    def rightRotate(self, x):
        """Performs a right rotation around the given node."""
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def leftRotate(self, x):
        """Performs a left rotation around the given node."""
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, node, key):
        """Brings the node with the given key to the root, if it exists."""
        if node is None or node.key == key:
            return node

        if node.key > key:
            if node.left is None:
                return node
            if node.left.key > key:
                node.left.left = self.splay(node.left.left, key)
                node = self.rightRotate(node)
            elif node.left.key < key:
                node.left.right = self.splay(node.left.right, key)
                if node.left.right:
                    node.left = self.leftRotate(node.left)
            return self.rightRotate(node) if node.left else node

        else:
            if node.right is None:
                return node
            if node.right.key > key:
                node.right.left = self.splay(node.right.left, key)
                if node.right.left:
                    node.right = self.rightRotate(node.right)
            elif node.right.key < key:
                node.right.right = self.splay(node.right.right, key)
                node = self.leftRotate(node)
            return self.leftRotate(node) if node.right else node

    def insert(self, key):
        """Inserts a node with the given key into the tree."""
        if not self.root:
            self.root = Node(key)
            return
        self.root = self.splay(self.root, key)
        if self.root.key == key:
            return  # Duplicate keys are not inserted in this tree
        new_node = Node(key)
        if self.root.key > key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def find(self, key):
        """Finds and splays the node with the given key."""
        self.root = self.splay(self.root, key)
        return self.root if self.root and self.root.key == key else None

    def preOrder(self, node):
        """Performs a preorder traversal of the tree starting from the given node."""
        result = []
        if node:
            result.append(node.key)
            result.extend(self.preOrder(node.left))
            result.extend(self.preOrder(node.right))
        return result

    def print_tree(self, node, level=0, prefix="Root: "):
        """Prints the tree structure."""
        if node:
            print(" " * (level * 4) + prefix + str(node.key))
            self.print_tree(node.left, level + 1, "L--- ")
            self.print_tree(node.right, level + 1, "R--- ")

    def remove(self, key):
        if not self.root:
            return
        self.root = self.splay(self.root, key)
        if self.root.key != key:
            return  # Key not found, no node to remove
        if not self.root.left:
            self.root = self.root.right
        else:
            right_subtree = self.root.right
            self.root = self.splay(self.root.left, key)  # Splay the maximum key in the left subtree
            self.root.right = right_subtree
        # The node is now removed from the tree

if __name__ == "__main__":
    # Manually creating the tree structure as described
    root = Node(3)
    root.left = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(2)
    root.right = Node(5)
    root.right.left = Node(4)
    root.right.right = Node(11)
    root.right.right.left = Node(7)
    root.right.right.right = Node(12)
    root.right.right.left.left = Node(6)
    root.right.right.left.right = Node(9)
    root.right.right.left.right.left = Node(8)
    root.right.right.left.right.right = Node(10)

    tree = SplayTree(root)

    # Print the tree after manual setup
    print("Tree structure after manual setup:")
    tree.print_tree(tree.root)

    # Find and splay operation
    print("\nAfter finding and splaying 10:")
    tree.find(10)
    tree.print_tree(tree.root)

    tree.remove(9)
    print("\nAfter removing 9:")
    tree.print_tree(tree.root)