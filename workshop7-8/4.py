"""
Generate all suffixes of the given string.
Insert each suffix into the tree, starting from the root. If a path already exists, follow it as far as possible and then create new nodes as needed.
Label the edges with the appropriate substring of the suffix being inserted.
"""
class TreeNode:
    def __init__(self, label=''):
        self.label = label
        self.children = {}

    def insert(self, suffix, full_suffix):
        if not suffix:  # Base case: no more suffix to insert.
            return
        for child in self.children:
            # If the suffix starts with child label, we need to split/join.
            if suffix.startswith(child):
                common_length = len(child)
                self.children[child].insert(suffix[common_length:], full_suffix)
                return
            elif child.startswith(suffix[0]):
                # Split edge.
                common_prefix = child[0]
                new_node = TreeNode(common_prefix)
                new_node.children[child[1:]] = self.children[child]
                new_node.children[suffix[1:]] = TreeNode(suffix[1:])
                del self.children[child]
                self.children[common_prefix] = new_node
                return
        # No common path, create a new edge.
        self.children[suffix] = TreeNode(suffix)

    def print_tree(self, level=0):
        for child in self.children:
            print('  ' * level + f'{child}')
            self.children[child].print_tree(level + 1)

def build_suffix_tree(s):
    root = TreeNode()
    for i in range(len(s)):
        suffix = s[i:]
        print(f'Inserting: {suffix}')
        root.insert(suffix, suffix)
        root.print_tree()
        print('---')
    return root

s = 'addaadd#'
tree = build_suffix_tree(s)
