"""
A standard trie is a tree-like data structure where each node represents a single character of a word. The trie supports fast lookup, insert, and delete operations, typically used for searching words in a dictionary.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

def build_standard_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def print_trie(node, prefix=''):
    if node.isEndOfWord:
        print('Word:', prefix)
    for char, next_node in node.children.items():
        print_trie(next_node, prefix + char)

words = ["exam", "example", "fail", "false", "tree", "trie", "true"]
standard_trie = build_standard_trie(words)
print("Standard Trie:")
print_trie(standard_trie.root)
"""
A trie with list nodes differs from a standard trie in that each node contains a list of child nodes instead of a dictionary. This structure might be less efficient in terms of lookup time but serves educational purposes.
"""

class ListNode:
    def __init__(self, char):
        self.char = char
        self.isEndOfWord = False
        self.children = []

class ListTrie:
    def __init__(self):
        self.root = ListNode("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            found_in_children = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_children = True
                    break
            if not found_in_children:
                new_node = ListNode(char)
                node.children.append(new_node)
                node = new_node
        node.isEndOfWord = True

def build_list_trie(words):
    trie = ListTrie()
    for word in words:
        trie.insert(word)
    return trie

def print_list_trie(node, prefix=''):
    if node.isEndOfWord:
        print('Word:', prefix)
    for child in node.children:
        print_list_trie(child, prefix + child.char)

list_trie = build_list_trie(words)
print("\nTrie with List Nodes:")
print_list_trie(list_trie.root)

"""
A Patricia Tree, or Radix Tree, compresses the standard trie by merging nodes with a single child. This structure is more space-efficient, especially when the dataset contains many common prefixes.
"""
class PatriciaNode:
    def __init__(self, key="", value=None):
        self.key = key
        self.value = value
        self.children = {}

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaNode()

    def insert(self, word):
        node = self.root
        while True:
            matched = False
            for child_key, child_node in node.children.items():
                if word.startswith(child_key):
                    matched = True
                    word = word[len(child_key):]
                    node = child_node
                    break
            if not matched:
                if word != "":
                    node.children[word] = PatriciaNode(key=word, value=True)
                break

def build_patricia_trie(words):
    trie = PatriciaTrie()
    for word in words:
        trie.insert(word)
    return trie

def print_patricia_trie(node, prefix=''):
    if node.value is not None:
        print('Word:', prefix + node.key)
    for child_key, child_node in node.children.items():
        print_patricia_trie(child_node, prefix + node.key)

patricia_trie = build_patricia_trie(words)
print("\nPatricia Trie:")
print_patricia_trie(patricia_trie.root)

