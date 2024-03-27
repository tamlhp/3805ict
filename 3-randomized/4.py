"""
- First Fit places each item into the first bin in which it fits. This approach is fast and straightforward 
but might not always lead to the most space-efficient arrangement.
- Best Fit places each item into the bin that will leave the least room left over after the item is placed. 
This can lead to more space-efficient packing than First Fit but may require more computation to find the 
best bin for each item.
"""


def first_fit(items, bin_capacity):
    bins = []
    
    for item in items:
        placed = False
        # Try to place item in existing bins
        for b in bins:
            if sum(b) + item <= bin_capacity:
                b.append(item)
                placed = True
                break
        # If item not placed, create a new bin
        if not placed:
            bins.append([item])
    
    return bins

items = [2, 5, 4, 7, 1, 3, 8]
bin_capacity = 10
bins = first_fit(items, bin_capacity)
print(f'First Fit Bins: {bins}')

def best_fit(items, bin_capacity):
    bins = []
    
    for item in items:
        # Find the best bin that can accommodate the item
        best_bin_index = -1
        min_space_left = float('inf')
        for i, b in enumerate(bins):
            space_left = bin_capacity - sum(b)
            if 0 < space_left - item < min_space_left:
                best_bin_index = i
                min_space_left = space_left - item
        # Place item in the best bin or start a new bin
        if best_bin_index >= 0:
            bins[best_bin_index].append(item)
        else:
            bins.append([item])
    
    return bins

items = [2, 5, 4, 7, 1, 3, 8]
bin_capacity = 10
bins = best_fit(items, bin_capacity)
print(f'Best Fit Bins: {bins}')

