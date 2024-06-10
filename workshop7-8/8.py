class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None
    
    # Alternate between x and y axis
    k = len(points[0])  # assumes all points have the same dimension
    axis = depth % k
    
    # Sort point list and choose median as pivot element
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    
    # Create node and construct subtrees
    return Node(
        point=points[median],
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median+1:], depth + 1)
    )

def print_tree(node, depth=0, prefix="Root:"):
    if node is not None:
        print("  " * depth + prefix + str(node.point))
        print_tree(node.left, depth + 1, "Left:")
        print_tree(node.right, depth + 1, "Right:")

def delete_point(points, point_to_delete):
    return [point for point in points if point != point_to_delete]

# Define points
points = [(5, 4), (2, 9), (3, 5), (2, 2), (9, 2), (6, 1), (9, 9)]

# Build kd-tree
kd_tree = build_kd_tree(points)

# Print the kd-tree structure
print("KD-tree structure:")
print_tree(kd_tree)

# Delete point E[9, 2] and rebuild the tree
points_after_deletion = delete_point(points, (9, 2))
kd_tree_after_deletion = build_kd_tree(points_after_deletion)

# Print the kd-tree after deletion
print("\nKD-tree after deleting E[9, 2]:")
print_tree(kd_tree_after_deletion)
