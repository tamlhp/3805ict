def ccw(A, B, C):
    """Check if the points are listed in counter-clockwise order."""
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def segments_intersect(seg1, seg2):
    """Check if two line segments intersect."""
    A, B = seg1[0], seg1[1]
    C, D = seg2[0], seg2[1]
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def is_simple_closed_polygon(segments):
    # Check if all endpoints are connected to exactly two segments
    endpoint_counts = {}
    for seg in segments:
        for point in [seg[0], seg[1]]:
            if point in endpoint_counts:
                endpoint_counts[point] += 1
            else:
                endpoint_counts[point] = 1
    
    if any(count != 2 for count in endpoint_counts.values()):
        return False  # Not all points connect to two segments
    
    # Check for any segment intersections, excluding shared endpoints
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if segments[i][0] != segments[j][0] and segments[i][1] != segments[j][1] and segments[i][0] != segments[j][1] and segments[i][1] != segments[j][0]:
                if segments_intersect(segments[i], segments[j]):
                    return False  # Found an intersection, not a simple polygon
    
    return True  # Passed both checks

# Example usage:
segments = [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (0, 0))]
print(is_simple_closed_polygon(segments))
