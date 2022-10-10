import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line_longer = False
    second_line_longer = False
    if (abs(x4 - x3) >= abs(x2 - x1) or abs(y4 - y3) >= abs(y2 - y1)) and \
            (abs(x4 - y3) >= abs(x2 - y1) or abs(y4 - x3) >= abs(y2 - x1)):
        second_line_longer = True
    else:
        first_line_longer = True
    if first_line_longer:
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
        return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
    else:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"
        return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"


point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())
point_x3 = float(input())
point_y3 = float(input())
point_x4 = float(input())
point_y4 = float(input())
print(longer_line(point_x1, point_y1, point_x2, point_y2, point_x3, point_y3, point_x4, point_y4))