import random

class Node:
    """A node in a skip list"""
    def __init__(self, key, level):
        self.key = key
        # Create forward references for each level
        self.forward = [None] * (level + 1)

class SkipList:
    """A simple implementation of a skip list"""
    def __init__(self, max_level):
        self.max_level = max_level
        # Create a header node with key -inf and max level
        self.header = self.create_node(-float('inf'), self.max_level)
        # The current highest level in the skip list
        self.level = 0
        
    def create_node(self, key, level):
        return Node(key, level)
    
    def random_level(self, seed):
        """Replace the random generator for consistent 'random' results"""
        random.seed(seed)  # Seed the random number generator
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
    
    def insert(self, key, seed):
        level = self.random_level(seed)
        new_node = self.create_node(key, level)
        current = self.header
        
        # Start from the highest level of the skip list and work down
        for i in reversed(range(self.max_level + 1)):
            # Find the correct position to insert the new node
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            # If the level is less than or equal to node's level, insert it
            if i <= level:
                new_node.forward[i] = current.forward[i]
                current.forward[i] = new_node
                
        # Update the current level of the skip list
        self.level = max(self.level, level)
        
    def display_list(self):
        print("\n*****Skip List******")
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.header.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")

# Create an instance of SkipList
skip_list = SkipList(4)

# Insert keys with the shown “randomly generated” values
keys = [5, 26, 25, 6, 21, 3, 22]
seeds = [1, 1, 4, 3, 1, 2, 2]

# Insert each key and display the state of the skip list after each insertion
for key, seed in zip(keys, seeds):
    skip_list.insert(key, seed)
    skip_list.display_list()
