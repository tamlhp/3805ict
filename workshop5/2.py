"""
1. Start with a Find: When you want to find which group an element belongs to, you start the path compression process.
2. Follow the Chain: You follow the chain of parent pointers from the element you're interested in all the way up to the root of the tree.
3. Reach the Root: Once you find the root (the boss of the group), you're nearly done.
4. Make a Shortcut: On the way back down from the root, you make every element you just visited point directly to the root.
5. Finished: Now the tree is flatter, and next time you need to find the root for any of these elements, it's much quicker because the path is shorter.
So, in essence, path compression is about making a "shortcut" straight to the top anytime you climb the tree to find the root.

Pseudocode for Find with Path Compression:

function Find(x)
    if x is not the root (parent[x] is not x)
        // Recursively find the root of x, and during the unwind of the recursion,
        // set each parent along the way to point directly to the root.
        parent[x] = Find(parent[x])  
    return parent[x]  // The root of x is returned


     1
    / \
   2   3
  /   / \
 4   5   6

After calling "find(4)" with path compression:
     1
    /|\
   2 3 4
    / \
   5   6

After calling "find(5)" with path compression:
     1
   /| |\
  2 3 4 5
       \
        6
"""

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))  # Everyone is their own parent initially.
    
    def find(self, x):
        if self.parent[x] != x:
            print(f"Element {x} is not the root. Its parent is {self.parent[x]}.")
            # Recursively find the root, and set the parent of x to be the root.
            # Path compression happens here.
            self.parent[x] = self.find(self.parent[x])
            print(f"Path compression: now element {x} points directly to the root {self.parent[x]}.")
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:  # If they're in different sets, join them.
            self.parent[root_y] = root_x  # Make one root point to the other.
            print(f"Union: Root of element {y} is now pointing to root of element {x}.")

    def print_sets(self):
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets:
                sets[root] = [i]
            else:
                sets[root].append(i)
        print("Disjoint Sets:")
        for root, elements in sets.items():
            print(f"Root {root}: {elements}")

# Example usage:
ds = DisjointSet(10)

# Union some sets.
ds.union(2, 4)
ds.union(3, 4)
ds.union(5, 6)
ds.union(5, 9)

# Now find the root of an element, which will also apply path compression.
print(f"Root of 5: {ds.find(5)}")
print(f"Root of 9: {ds.find(9)}")
print(f"Root of 4: {ds.find(4)}")

# Finally, print all the sets.
ds.print_sets()
