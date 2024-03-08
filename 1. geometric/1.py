"""
The CCW function will return a positive value if the point c is to 
the left of the line ab, a negative value if the point c is to the right, 
and zero if the points are collinear.
"""
def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def counter_clockwise(a, b, c):
    value = ccw(a, b, c)
    if value > 0: return "CW"
    if value < 0: return "CCW"
    return "Collinear"

# Another way for intersection
# def intersect(seg1, seg2):
#     A, B = seg1[0], seg1[1]
#     C, D = seg2[0], seg2[1]
#     return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def intersect(p1, q1, p2, q2):
    # Check if the orientation of all combinations of three points is different
    # Line segments intersect if both endpoints of each line are on different “sides” (have different counter_clockwise values) of the other then the lines must intersect.
    o1 = ccw(p1, q1, p2)
    o2 = ccw(p1, q1, q2)
    o3 = ccw(p2, q2, p1)
    o4 = ccw(p2, q2, q1)
    
    return (o1 * o2 < 0 and o3 * o4 < 0)

def is_closed_simple_path(points):
    # Check if the path is closed
    if points[0] != points[-1]:
        return False
    
    # Check for intersections
    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if intersect(points[i], points[(i + 1) % (n - 1)], points[j], points[(j + 1) % (n - 1)]):
                return False
    return True

def is_point_in_polygon(point, polygon):
    """
    Determine if a point is inside a given polygon or not
    Polygon is a list of (x,y) pairs. This function returns True if the point is inside the polygon and False otherwise.
    """
    x, y = point
    num = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(num+1):
        p2x, p2y = polygon[i % num]
        if y > min(p1y, p2y):  # Check if the point's y-coordinate is above the lower end of the edge.
            if y <= max(p1y, p2y):  # Check if the point's y-coordinate is below the higher end of the edge.
                if x <= max(p1x, p2x):  # Check if the point's x-coordinate is to the left of the edge.
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:  # If the point is on the segment or to the left of the intersection point.
                            inside = not inside
                    else:
                        # For a horizontal edge, we do not alter the 'inside' status,
                        # but we need to handle cases where the point is exactly on a horizontal edge.
                        # This case is implicitly handled by the edge's bounds checks and does not require further action.
                        pass
        p1x, p1y = p2x, p2y # Move to the next segment of the polygon.
    return inside

# Test data
a = (0, 0)
b = (4, 4)
c = (1, 1)
d = (1, 0)
e = (0, 1)
p = (2, 2)
polygon = [a, e, b, d, c, a]

# Testing CCW
print("CCW:", counter_clockwise(a, d, p))

# Testing Intersect
print("Intersect:", intersect(a, b, c, a))

# Testing Closed Simple Path
print("Closed Simple Path:", is_closed_simple_path(polygon))

# Testing Point in Polygon
print("Point in Polygon:", is_point_in_polygon(p, [a,b,c]))  # Remove the last point as it is a duplicate of the first