import random

"""
- Using the number of accesses as a priority (not implemented here) would involve updating a node's priority 
each time it's accessed and then performing the necessary tree rotations to maintain the heap property. This could make frequently accessed nodes more accessible but at the cost of potential loss of balance in terms of tree height.

- Generating a random number each time an item is accessed and possibly updating its priority could help in 
certain scenarios where the access pattern is non-uniform. If a lower priority is assigned, the node would 
be rotated up to maintain the min-heap property, potentially making future accesses faster. This method 
maintains more of the random nature of a treap.

The randomised strategy inherent to treaps ensures a balanced structure on average, making the treap a simple 
and efficient self-balancing tree. The self-adjusting strategies mentioned would aim to improve the treap's performance 
for specific access patterns but may not maintain the same probabilistic balance as a standard treap.


Access-Based Priority Adjustment:

Pros: Adapts to access patterns, improving performance for frequently accessed elements. Predictable behavior.
Cons: May not optimize as well for varied or unpredictable access patterns.
Randomized Priority Adjustment:

Pros: Can introduce beneficial randomness, potentially leading to a well-balanced tree in varied access scenarios. Unpredictable, which might occasionally outperform access-based adjustments.
Cons: Less predictable performance. Adjustments do not directly reflect access frequency, potentially leading to less optimization for frequent accesses.
"""

import random

class TreapNode:
    def __init__(self, key, priority=0):
        self.key = key
        self.priority = priority
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

# METHOD 1
def access_and_adjust(root, key):
    if not root or root.key == key:
        if root:
            root.priority += 1  # Increment access count
        return root
    
    if key < root.key:
        root.left = access_and_adjust(root.left, key)
        if root.left and root.left.priority > root.priority:
            root = right_rotate(root)
    else:
        root.right = access_and_adjust(root.right, key)
        if root.right and root.right.priority > root.priority:
            root = left_rotate(root)
    return root

# METHOD 2
def access_and_adjust(root, key):
    if not root or root.key == key:
        if root:
            root.priority += 1  # Increment access count for demonstration
            new_priority = random.randint(1, 100)  # Generate a new random priority
            if new_priority < root.priority:  # If new priority is lower, update and possibly rotate
                root.priority = new_priority
                # No need to rotate here since this node is already at the accessed position,
                # but in a full implementation, rotations might be considered to adjust the tree structure.
        return root
    
    if key < root.key:
        root.left = access_and_adjust(root.left, key)
        if root.left and root.left.priority > root.priority:
            root = right_rotate(root)
    else:
        root.right = access_and_adjust(root.right, key)
        if root.right and root.right.priority > root.priority:
            root = left_rotate(root)
    return root

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + f"Key: {node.key}, Priority: {node.priority}")
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# Example usage
root = TreapNode(50, 1)
root.left = TreapNode(30, 1)
root.right = TreapNode(70, 1)
root.left.left = TreapNode(20, 1)
root.left.right = TreapNode(40, 1)
root.right.left = TreapNode(60, 1)
root.right.right = TreapNode(80, 1)

# Access nodes and adjust
keys_to_access = [20, 30, 70, 50]
for key in keys_to_access:
    print(f"Accessing and adjusting {key}")
    root = access_and_adjust(root, key)
    print_tree(root)
    print("------")