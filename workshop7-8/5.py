class TreeNode:
    def __init__(self, label=''):
        self.label = label  # Edge label
        self.children = {}  # Dictionary to hold children

    def insert(self, suffix):
        if not suffix:
            return
        found = False
        for child in self.children:
            if suffix[0] == child[0]:  # Check if a child with the same starting letter exists
                found = True
                self.children[child].insert(suffix[1:])  # Recurse with the rest of the suffix
                break
        if not found:
            self.children[suffix] = TreeNode(suffix)  # No matching child, create a new one

    def print_tree(self, level=0):
        for child in self.children:
            print(' ' * level + '|--' + child)
            self.children[child].print_tree(level + 4)  # Indent for visual hierarchy

def build_suffix_tree(s):
    root = TreeNode()
    for i in range(len(s)):
        suffix = s[i:]  # Extract suffix starting at position i
        root.insert(suffix)  # Insert suffix into tree
    return root

# Given string S
S = "AAATCTTCC"
# Build the suffix tree
tree = build_suffix_tree(S)
# Print the tree structure
tree.print_tree()


"""
Suffix Tree Construction: The construction time of a suffix tree for a text of length m can be O(m) using advanced 
algorithms like Ukkonen's algorithm. This is a preprocessing step and does not depend on the pattern length n.
Pattern Searching: Once the suffix tree is constructed, searching for a pattern of length n within this tree has a 
time complexity of O(n). This efficiency comes from the fact that each step of the search process moves down the tree 
from one node to the next by following the edge that matches the next character of the pattern. Since the tree represents 
all possible suffixes of the text, if the pattern exists in the text, it will be found along some path from the root to a 
leaf (or a node, if the pattern is also a prefix of a longer suffix in the text).
"""