"""
- Convex Polygon: A ray can intersect the boundary of a convex polygon at most twice because, 
by definition, a convex polygon is one where a line segment between any two points in the polygon lies entirely within the polygon. 
Thus, a ray from outside cannot enter the polygon more than once without exiting. 
- Concave Polygon: The maximum achievable theoretically is N when the 
polygon is constructed in a specific way to allow a ray to pass through each vertex or edge.
"""

def count_ray_intersections(point, polygon):
    x, y = point
    num = len(polygon)
    count = 0

    p1x, p1y = polygon[0]
    for i in range(num + 1):
        p2x, p2y = polygon[i % num]
        if y > min(p1y, p2y) and y <= max(p1y, p2y):
            if x < max(p1x, p2x):
                if p1y != p2y:
                    xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        count += 1
        p1x, p1y = p2x, p2y

    return count

# Convex polygon example (square)
convex_polygon = [(0, 0), (10, 0), (10, 10), (0, 10)]

# Concave polygon example ("zigzag" shape for demonstration)
concave_polygon = [(0, 3), (1, 2), (2, 3), (1, 0)]

# Point for ray casting (sufficiently to the left of both polygons)
point = (-1, 2.5)  # y-coordinate chosen to intersect all "zigzag" edges
# point = (0.5, 2)

# Count intersections for convex polygon
convex_intersections = count_ray_intersections(point, convex_polygon)
print(f"Number of intersections with convex polygon: {convex_intersections}")

# Count intersections for concave polygon
concave_intersections = count_ray_intersections(point, concave_polygon)
print(f"Number of intersections with concave polygon: {concave_intersections}")
