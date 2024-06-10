"""


Class VEBTree
    Initialize(u):
        Set universe size u
        Set min and max to None
        If u > 2:
            Calculate cluster_count as sqrt(u)
            Initialize clusters array of size cluster_count to None
            Initialize summary to None

    Method insert(x):
        If tree is empty:
            Set min and max to x
        Else:
            If x < min:
                Swap x and min
            If u > 2:
                Determine cluster (high) and position (low) for x
                If cluster does not exist:
                    Create new vEBTree for cluster
                If summary does not exist:
                    Create new vEBTree for summary
                Insert low part of x into the identified cluster
                Insert cluster index into summary
            Update max if x > max

    Method print_tree(prefix):
        Print min and max with prefix
        If u > 2:
            Print summary tree with prefix '  S-'
            For each cluster:
                If cluster is not empty:
                    Recursively print cluster with prefix '  C[i]-'
"""


class VEBTree:
    def __init__(self, u):
        self.u = u  # Universe size
        self.min = None
        self.max = None
        if u > 2:
            self.cluster_count = int(u**0.5)
            self.clusters = [None] * self.cluster_count
            self.summary = None

    def high(self, x):
        return x // self.cluster_count

    def low(self, x):
        return x % self.cluster_count

    def index(self, x, y):
        return x * self.cluster_count + y

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        else:
            if x < self.min:
                x, self.min = self.min, x  # Swap x and self.min
            if self.u > 2:
                high = self.high(x)
                low = self.low(x)
                if self.clusters[high] is None:
                    self.clusters[high] = VEBTree(self.cluster_count)
                if self.summary is None:
                    self.summary = VEBTree(self.cluster_count)
                self.clusters[high].insert(low)
                self.summary.insert(high)
            if x > self.max:
                self.max = x

    def print_tree(self, prefix=''):
        print(f"{prefix}min: {self.min}, max: {self.max}")
        if self.u > 2:
            if self.summary:
                self.summary.print_tree(prefix + '  S-')
            for i, cluster in enumerate(self.clusters):
                if cluster is not None:
                    cluster.print_tree(prefix + f'  C{i}-')

# Universe size 16, storing the set {1, 3, 4, 7, 9, 11, 12, 13}
u_size = 16
elements = {1, 3, 4, 7, 9, 11, 12, 13}
veb_tree = VEBTree(u_size)

for elem in elements:
    veb_tree.insert(elem)

veb_tree.print_tree()
