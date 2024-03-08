"""
To determine if four line segments form a square without using division, we need to check a few things:
- All segments are of equal length.
- The segments form right angles at their intersections.
Without division, we can check if the segments are of equal length by comparing their squared lengths. To ensure the segments form right angles, we can use the dot product of vectors; if two vectors are perpendicular, their dot product is zero.
"""

def squared_distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def dot_product(x1, y1, x2, y2, x3, y3):
    # Vector from (x1, y1) to (x2, y2)
    vx1 = x2 - x1
    vy1 = y2 - y1
    # Vector from (x1, y1) to (x3, y3)
    vx2 = x3 - x1
    vy2 = y3 - y1
    # Dot product
    return vx1 * vx2 + vy1 * vy2

def is_square(p1, p2, p3, p4):
    # Calculate squared lengths of all sides
    d1 = squared_distance(*p1, *p2)
    d2 = squared_distance(*p2, *p3)
    d3 = squared_distance(*p3, *p4)
    d4 = squared_distance(*p4, *p1)
    
    # Check if all sides have equal length
    if d1 == d2 == d3 == d4:
        # Calculate squared lengths of diagonals
        diag1 = squared_distance(*p1, *p3)
        diag2 = squared_distance(*p2, *p4)
        
        # Check if diagonals are equal in length, implies right angles
        if diag1 == diag2:
            # Further check to ensure the angles between sides are right angles
            if not dot_product(*p1, *p2, *p4) and not dot_product(*p2, *p3, *p1):
                return True
    return False

# Example usage
p1 = (0, 0)
p2 = (0, 1)
p3 = (1, 1)
p4 = (1, 0)
print(is_square(p1, p2, p3, p4))  # Should return True
