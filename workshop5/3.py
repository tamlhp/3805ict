"""
The second requirement asks for both the weighted union heuristic and path compression to be implemented. 
This means that every time two sets are united, the smaller set (by weight or rank) should be attached to the larger one, 
and whenever a "find" operation is executed, path compression should be applied. This combination of optimizations 
ensures that the tree's height is kept to a minimum, making the union and find operations very efficient even for 
large data sets.

1. Count Members: Keep track of the size (number of members) of each tree.
2. Find Roots: When you want to combine two trees, first find the root of each tree.
3. Compare Sizes: Check which tree is smaller by comparing their sizes.
4. Attach Smaller to Larger: Attach the smaller tree to the root of the larger tree.
5. Update Size: Update the size of the new combined tree.
By following these steps, you prevent the trees from becoming too tall, which helps to keep the time it takes to find the root of any member low.

Pseudocode for Weighted Union Heuristic:

function Union(x, y)
    rootX = Find(x)
    rootY = Find(y)

    if rootX is not rootY
        if size[rootX] < size[rootY]
            parent[rootX] = rootY
            size[rootY] = size[rootY] + size[rootX]
        else
            parent[rootY] = rootX
            size[rootX] = size[rootX] + size[rootY]
"""

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.weight = [1] * size  # Initialize the weight for each node to be 1
    
    def find(self, x):
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            print(f"Path compression: Element {x} now points directly to the root {self.parent[x]}, "
                  f"was pointing to {original_parent}.")
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Attach the smaller weight tree to the larger weight tree
            if self.weight[root_x] < self.weight[root_y]:
                self.parent[root_x] = root_y
                self.weight[root_y] += self.weight[root_x]
                print(f"Union: Root of element {x} (tree weight {self.weight[root_x]}) is now pointing to "
                      f"root of element {y} (tree weight {self.weight[root_y]}).")
            else:
                self.parent[root_y] = root_x
                self.weight[root_x] += self.weight[root_y]
                print(f"Union: Root of element {y} (tree weight {self.weight[root_y]}) is now pointing to "
                      f"root of element {x} (tree weight {self.weight[root_x]}).")

    def print_sets(self):
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)  # This will also cause path compression
            if root not in sets:
                sets[root] = [i]
            else:
                sets[root].append(i)
        print("Disjoint Sets after Weighted Union and Path Compression:")
        for root, elements in sets.items():
            print(f"Set led by {root}: {elements}")

# Example usage
dsu = DisjointSet(10)

# Perform some unions with prints
print("Performing Unions:")
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(0, 3)
dsu.union(4, 5)
dsu.union(6, 7)
dsu.union(8, 9)
dsu.union(4, 9)
dsu.union(0, 9)

# Finding elements with path compression prints
print("\nFinding elements with path compression:")
print(f"Find(2): {dsu.find(2)}")
print(f"Find(8): {dsu.find(8)}")
print(f"Find(9): {dsu.find(9)}")

# Print the sets after the unions and finds
print("\nFinal Disjoint Sets:")
dsu.print_sets()