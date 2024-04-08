"""
Yes, the order of additions and deletions to a treap can indeed change the final structure of the treap. This behavior is due to the intrinsic properties of treaps, which combine aspects of binary search trees (BSTs) and heaps:

Binary Search Tree (BST) Property: This ensures that for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater. When you add or delete nodes, you must maintain this property, which may involve reordering elements.
Heap Property: Each node in a treap is assigned a priority, typically based on random generation, and the treap maintains the heap property based on these priorities. Specifically, a node's priority must be higher than that of its children. This property may necessitate rotations during additions and deletions to maintain a valid treap structure.
"""

import random

class TreapNode:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = random.randint(1, 100) if priority is None else priority
        self.left = None
        self.right = None

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    return y

def insert(root, key):
    if not root:
        return TreapNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.priority > root.priority:
            root = right_rotate(root)
    else:
        root.right = insert(root.right, key)
        if root.right and root.right.priority > root.priority:
            root = left_rotate(root)
    return root

def delete(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:  # root.key == key
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        elif root.left.priority < root.right.priority:
            root = left_rotate(root)
            root.left = delete(root.left, key)
        else:
            root = right_rotate(root)
            root.right = delete(root.right, key)
    return root

def print_tree(node, prefix="", is_left=True):
    if node:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + f"Key: {node.key}, Priority: {node.priority}")
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# Initial sequence of operations
print("Initial sequence of operations:")
root = None
for key in [5, 2, 8, 6, 3]:
    root = insert(root, key)

for key in [8, 2]:
    root = delete(root, key)

print_tree(root)
print("------")

# Reset root for a different sequence
root = None

# Different sequence of operations
print("Different sequence of operations:")
for key in [2, 6, 3, 5, 8]:  # Different order of insertion
    root = insert(root, key)

for key in [2, 8]:  # Same deletions for comparison
    root = delete(root, key)

print_tree(root)
