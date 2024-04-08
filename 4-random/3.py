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
        self.header = self.create_node(-float('inf'), self.max_level)
        self.level = 0

    def create_node(self, key, level):
        return Node(key, level)

    def random_level(self, seed):
        random.seed(seed)
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key, seed):
        level = self.random_level(seed)
        new_node = self.create_node(key, level)
        current = self.header

        for i in reversed(range(self.max_level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            if i <= level:
                new_node.forward[i] = current.forward[i]
                current.forward[i] = new_node

        self.level = max(self.level, level)

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        next_node = current.forward[0]
        if next_node and next_node.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != next_node:
                    break
                update[i].forward[i] = next_node.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display_list(self):
        print("\n*****Skip List******")
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = self.header.forward[lvl]
            while(node is not None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")

# Initialize the skip list
skip_list = SkipList(4)

# Insert keys with the shown “randomly generated” values
keys = [5, 26, 25, 6, 21, 3, 22]
seeds = [1, 1, 4, 3, 1, 2, 2]

# Insert each key
for key, seed in zip(keys, seeds):
    skip_list.insert(key, seed)

# Display the skip list after all insertions
skip_list.display_list()

# Perform deletions in the order listed above
for key in keys:
    skip_list.delete(key)
    skip_list.display_list()
