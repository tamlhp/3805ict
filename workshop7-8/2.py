"""
Start with an Empty Tree: Initially, the Splay Tree is empty.
Insert the First Key (4): Since the tree is empty, the first key becomes the root. No splaying is needed.
Insert the Second Key (9): Insert the key as you would in a binary search tree (BST), then splay it to the root.
Insert Subsequent Keys (3, 7, 5, 6): For each key:
Insert the key into the tree following BST rules.
Splay the tree at the inserted key, moving it to the root.
Splaying: If the inserted node's parent is the root, perform a single rotation (zig or zag). If the inserted node has a grandparent, choose the appropriate double rotation (zig-zig, zig-zag, zag-zig, or zag-zag) based on the node's and its parent's positions relative to their parents.
Show Intermediate Trees: After each insertion and splaying, print the tree to show its structure at that stage.

Function InsertSplayTree(root, key)
    If root is nil
        root = newNode(key)
    Else
        Insert key using BST insertion rules
        Splay the tree at the inserted node

Function Splay(node)
    While node is not root
        If node's parent is root
            Perform zig or zag (single rotation)
        Else
            Perform zig-zig, zig-zag, zag-zig, or zag-zag (double rotation) as appropriate
        EndIf
    EndWhile

Main
    Initialize an empty Splay Tree
    For each key in [4, 9, 3, 7, 5, 6]
        InsertSplayTree(root, key)
        Print the tree
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def rightRotate(x):
    y = x.left
    x.left = y.right
    if y.right: y.right.parent = x
    y.parent = x.parent
    if not x.parent: root = y
    elif x == x.parent.right: x.parent.right = y
    else: x.parent.left = y
    y.right = x
    x.parent = y
    return y

def leftRotate(x):
    y = x.right
    x.right = y.left
    if y.left: y.left.parent = x
    y.parent = x.parent
    if not x.parent: root = y
    elif x == x.parent.left: x.parent.left = y
    else: x.parent.right = y
    y.left = x
    x.parent = y
    return y

def splay(node):
    while node.parent:
        if not node.parent.parent:
            if node == node.parent.left:
                rightRotate(node.parent)
            else:
                leftRotate(node.parent)
        elif node == node.parent.left and node.parent == node.parent.parent.left:
            rightRotate(node.parent.parent)
            rightRotate(node.parent)
        elif node == node.parent.right and node.parent == node.parent.parent.right:
            leftRotate(node.parent.parent)
            leftRotate(node.parent)
        elif node == node.parent.right and node.parent == node.parent.parent.left:
            leftRotate(node.parent)
            rightRotate(node.parent)
        else:
            rightRotate(node.parent)
            leftRotate(node.parent)

def insert(root, key):
    if not root: return Node(key)
    cur = root
    while True:
        if key < cur.key:
            if cur.left: cur = cur.left
            else:
                cur.left = Node(key)
                cur.left.parent = cur
                splay(cur.left)
                break
        else:
            if cur.right: cur = cur.right
            else:
                cur.right = Node(key)
                cur.right.parent = cur
                splay(cur.right)
                break
    while cur.parent: cur = cur.parent
    return cur

def printTree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level*4) + prefix + str(node.key))
        if node.left: printTree(node.left, level+1, "L--- ")
        if node.right: printTree(node.right, level+1, "R--- ")

keys = [4, 9, 3, 7, 5, 6]
root = None

for key in keys:
    root = insert(root, key)
    print(f"After inserting {key}:")
    printTree(root)
    print("---------------------")
