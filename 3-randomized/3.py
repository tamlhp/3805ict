"""
The Greedy algorithm for the Set Cover problem works by iteratively picking the set that covers 
the largest number of uncovered elements until all elements are covered. The Set Cover problem is defined 
as follows: Given a universe of elements and a collection of sets containing these elements, find the smallest 
subset of sets such that every element in the universe is included in at least one of the selected sets.
"""

def greedy_set_cover(universe, subsets):
    # Copy the universe and subsets to avoid side-effects
    universe = set(universe)
    subsets = list(subsets)
    cover = []

    # Continue until all elements are covered
    while universe:
        # Select the subset that covers the most uncovered elements
        subset = max(subsets, key=lambda s: len(s & universe))
        cover.append(subset)
        # Remove covered elements from the universe
        universe -= subset
        # Optional: Remove the chosen subset from the list of subsets
        subsets.remove(subset)

    return cover

# Example usage
universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
cover = greedy_set_cover(universe, subsets)

print("Selected Subsets for Cover:", cover)
