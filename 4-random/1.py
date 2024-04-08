class Node:
    """A node in a skip list"""
    def __init__(self, value, level):
        self.value = value
        # Create forward references for each level
        self.forward = [None] * (level + 1)

class SkipList:
    """A simple implementation of a skip list"""
    def __init__(self, max_level):
        self.max_level = max_level
        # Create a header node with value -inf and max level
        self.header = self.create_node(-float('inf'), self.max_level)
        # The current highest level in the skip list
        self.level = 0
        
    def create_node(self, value, level):
        return Node(value, level)
    
    def insert(self, value, level):
        # Create a new node with the specified value and level
        new_node = self.create_node(value, level)
        current = self.header
        
        # Start from the highest level of the skip list and work down
        for i in reversed(range(self.max_level + 1)):
            # Find the correct position to insert the new node
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            # If the level is less than or equal to node's level, insert it
            if i <= level:
                new_node.forward[i] = current.forward[i]
                current.forward[i] = new_node
                
        # Update the current level of the skip list
        self.level = max(self.level, level)
    
    def search(self, value):
        current = self.header
        path = []  # To store the path taken to find the value
        # Start from the highest level of the skip list and work down
        for i in reversed(range(self.level + 1)):
            # Move forward while the next node's value is less than the search value
            while current.forward[i] and current.forward[i].value < value:
                path.append(current.forward[i].value)  # Add to path
                current = current.forward[i]
        # Move to the node's next reference (down to the base level)
        current = current.forward[0]
        if current and current.value == value:
            path.append(current.value)  # Add to path
            return True, path
        else:
            return False, path

# Create a skip list based on the given image
skip_list = SkipList(5)
# Insert nodes with the appropriate levels
nodes = [
    (12, 2), (17, 5), (20, 1), (25, 4), (31, 3), 
    (38, 2), (39, 1), (44, 2), (50, 1), (55, 4)
]
for value, level in nodes:
    skip_list.insert(value, level)

# Search for 50 in the skip list and print the result
found, path = skip_list.search(50)
print(f"Search for 50: {'Found' if found else 'Not Found'}")
print(f"Path to 50: {path}")
