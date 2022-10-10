import math


def cartesian_coordinate_system(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    return f"({math.floor(x2)}, {math.floor(y2)})"


point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
print(cartesian_coordinate_system(point_x1, point_y1, point_x2, point_y2))