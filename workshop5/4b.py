"""
1. Find the Node: Locate the node with the key you want to decrease (666 in this case).
2. Decrease the Key: Change the key of the node to the new value (466).
3. Check the Min-Heap Property: If the new key is still greater than or equal to the parent's key, you're done. If it's less, proceed to the next step.
4. Cut and Promote: Remove the node from its current position and add it to the root list of the heap.
5. Cascading Cut: If the parent of the cut node is not a root and it's marked, cut the parent as well. Continue this process until you reach an unmarked node or a root.
6. Update Minimum: If the new key is less than the current minimum, update the minimum pointer.

function DecreaseKey(heap, node, new_key)
    if new_key >= node.key
        throw error "New key is greater than current key"
    node.key = new_key
    if node.parent and node.key < node.parent.key
        Cut(heap, node)
        CascadingCut(heap, node.parent)
    if node.key < heap.min.key
        heap.min = node

function Cut(heap, node)
    remove node from its parent's children
    add node to the root list
    node.marked = False

function CascadingCut(heap, node)
    while node is not a root and node is marked
        let parent = node.parent
        Cut(heap, node)
        node = parent
    if node is not a root
        node.marked = True


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

    def insert(self, node):
        self.roots.append(node)
        if not self.min or node.key < self.min.key:
            self.min = node

    def decrease_key(self, node, new_key):
        if new_key >= node.key:
            raise ValueError("New key must be smaller than current key.")

        node.key = new_key
        parent = node.parent

        if parent and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)

        if node.key < self.min.key:
            self.min = node

    def cut(self, node, parent):
        parent.children.remove(node)
        node.parent = None
        self.roots.append(node)
        node.marked = False
        parent.degree -= 1

    def cascading_cut(self, node):
        while node.parent:
            parent = node.parent
            if not node.marked:
                node.marked = True
                return
            self.cut(node, parent)
            node = parent

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

# Function to find a node with a specific key in the heap (for demonstration purposes)
def find_node(node, key):
    if node.key == key:
        return node
    for child in node.children:
        result = find_node(child, key)
        if result:
            return result
    return None

# Decrease the key of node 666 to 466
node_to_decrease = find_node(node1, 666)  # Start searching from the root node
if node_to_decrease:
    print(f"Found node with key {node_to_decrease.key}. Decreasing key to 466.")
    fib_heap.decrease_key(node_to_decrease, 466)
    print(f"Key decreased. New key is {node_to_decrease.key}.")

print(f"The minimum value in the heap is now: {fib_heap.min.key}")
