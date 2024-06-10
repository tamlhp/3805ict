"""
In a Red-Black Tree, which is a kind of self-balancing binary search tree, the maximum height depends on the number of nodes and the properties that the tree must maintain:

Every node is either red or black: This gives the tree its name.
The root is always black: This is a key property of the tree.
All leaves (NIL nodes) are black: Leaves are the empty nodes at the ends of the tree.
If a node is red, both its children are black: This prevents two red nodes from being connected.
Every path from a node to its descendant NIL nodes has the same number of black nodes: This is called the "black-height".
The properties ensure that the longest possible path from the root to a leaf (the tree's height) is no more than twice the length of the shortest possible path (the black-height). This is because the shortest possible path has all black nodes, and the longest path alternates between red and black nodes.

Given these properties, the maximum height h of a Red-Black Tree with n nodes can be roughly estimated by the formula:
h <= 2 * math.floor(math.log2(n + 1))
"""

import math

def max_height_red_black_tree(n):
    # The maximum height of a red-black tree is 2 times the black-height
    # Black-height can be calculated as floor(log2(n + 1))
    # Hence, we use the formula: h <= 2 * floor(log2(n + 1))
    return 2 * math.floor(math.log2(n + 1))

# Number of nodes
n = 14
# Calculate the maximum height of the red-black tree with n nodes
height = max_height_red_black_tree(n)

print(f"The maximum height of a Red-Black Tree with {n} nodes is: {height}")
