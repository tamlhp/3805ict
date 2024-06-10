"""
1. Find and Remove Minimum: Locate the tree with the smallest root (that's the minimum node). Remove this node from the heap.
2. Promote Children: If the minimum node has any children, they get promoted. This means they become top-level trees in the heap.
3. Clear Marks and Parents: Any child of the removed node now has no parent and if they were marked, we unmark them.
4. Consolidate Trees: Go through the trees in the top level and merge any that have the same degree, which means they have the same number of children. You keep merging until no two trees have the same degree.
5. Find New Min: Look through all the top-level nodes and find the smallest one. This is your new minimum.

Pseudocode for Delete-Min in a Fibonacci Heap:

function DeleteMin(heap)
    minNode = heap.min
    for each child of minNode
        add child to the root list of heap
        child.parent = NULL
        if child is marked
            unmark child
    remove minNode from the root list of heap
    consolidate(heap)
    findNewMin(heap)

function consolidate(heap)
    for each node in the root list
        while there exists another node with the same degree
            merge the two nodes
        update degree information

function findNewMin(heap)
    heap.min = NULL
    for each node in the root list
        if heap.min is NULL or node.key < heap.min.key
            heap.min = node
"""
class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.marked = False
        self.parent = None
        self.degree = 0

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.roots = []

    def delete_min(self):
        min_node = self.min
        print(f"Removing the minimum node: {min_node.key}")
        for child in min_node.children:
            print(f"Promoting child {child.key} to the root list.")
            self.roots.append(child)
            child.parent = None
            if child.marked:
                print(f"Unmarking node {child.key}.")
                child.marked = False
        self.roots.remove(min_node)
        self.min = None
        for node in self.roots:
            print(f"Considering node {node.key} as new minimum candidate.")
            if self.min is None or node.key < self.min.key:
                print(f"Node {node.key} is now the new minimum.")
                self.min = node
        return self.min

    def insert(self, node):
        self.roots.append(node)
        if not self.min or node.key < self.min.key:
            self.min = node

# Create the nodes as per the given structure
node1 = FibonacciHeapNode(1)
node4 = FibonacciHeapNode(4)
node7 = FibonacciHeapNode(7)
node19 = FibonacciHeapNode(19)
node5 = FibonacciHeapNode(5)
node9 = FibonacciHeapNode(9)
node12 = FibonacciHeapNode(12)
node8 = FibonacciHeapNode(8)
node13 = FibonacciHeapNode(13)
node666 = FibonacciHeapNode(666)
node667 = FibonacciHeapNode(667)
node668 = FibonacciHeapNode(668)
node10 = FibonacciHeapNode(10)
node11 = FibonacciHeapNode(11)
node14 = FibonacciHeapNode(14)
node8.marked = True
node10.marked = True
node11.marked = True
node13.marked = True
node667.marked = True


# Establish the relationships
node1.children = [node4, node7]
node4.children = [node8]
node8.children = [node10, node13]
node13.children = [node666]
node666.children = [node667, node668]
node10.children = [node11, node14]
node7.children = [node19]
node5.children = [node9, node12]

# Create the heap and set the minimum
fib_heap = FibonacciHeap()
fib_heap.insert(node1)  # This would be more complex in a real implementation
fib_heap.insert(node5)  # These nodes would be linked in a list, not just appended

# Now, we'll simulate the delete-min operation and output the steps.
print("Performing Delete-Min Operation...")
new_min = fib_heap.delete_min()
print(f"The new minimum value in the heap is: {new_min.key if new_min else 'undefined'}")