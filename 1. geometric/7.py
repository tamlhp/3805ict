import math

# Helper function to calculate distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute force method to find distance and pair of closest points in a set of points
def brute_force(P):
    min_dist = float('inf')
    closest_pair = (None, None)
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
                closest_pair = (P[i], P[j])
    return min_dist, closest_pair

# DIVIDE AND CONQUER
# Find the closest points straddling the dividing line
def strip_closest(strip, d, closest_pair):
    min_d = d
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_d:
            if dist(strip[i], strip[j]) < min_d:
                min_d = dist(strip[i], strip[j])
                closest_pair = (strip[i], strip[j])
            j += 1
    return min_d, closest_pair

# Recursive function to find the smallest distance and pair of closest points
def closest_pair_rec(Px, Py):
    # If the point set is small, use brute force
    if len(Px) <= 3:
        return brute_force(Px)
    
    # Divide the set in two halves
    mid = len(Px) // 2
    Qx = Px[:mid]
    Rx = Px[mid:]
    
    midpoint = Px[mid][0]  # Determine midpoint on x-axis
    Qy, Ry = [], []
    for point in Py:
        if point[0] <= midpoint:
            Qy.append(point)
        else:
            Ry.append(point)
    
    # Recursive calls
    d1, closest_pair_q = closest_pair_rec(Qx, Qy)
    d2, closest_pair_r = closest_pair_rec(Rx, Ry)
    if d1 < d2:
        d = d1
        closest_pair = closest_pair_q
    else:
        d = d2
        closest_pair = closest_pair_r
    
    # Create strip
    strip = [p for p in Py if abs(p[0] - midpoint) <= d]
    
    # Find the closest points in strip
    d_strip, strip_pair = strip_closest(strip, d, closest_pair)
    if d_strip < d:
        return d_strip, strip_pair
    else:
        return d, closest_pair

# Main function to find the closest pair of points and their distance
def closest_pair(P):
    Px = sorted(P, key=lambda x: x[0])  # Sort by x-coordinate
    Py = sorted(P, key=lambda x: x[1])  # Sort by y-coordinate
    return closest_pair_rec(Px, Py)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("Brute Force: ", brute_force(points))
print("Divide and Conquer: ", closest_pair(points))