import math
def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):

    x1, y1 = math.floor(x1), math.floor(y1)
    x2, y2 = math.floor(x2), math.floor(y2)
    x3, y3 = math.floor(x3), math.floor(y3)
    x4, y4 = math.floor(x4), math.floor(y4)

    first_line_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    second_line_length = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)

    def distance_to_center(x, y):
        return math.sqrt(x**2 + y**2)

    if first_line_length >= second_line_length:
        if distance_to_center(x1, y1) <= distance_to_center(x2, y2):
            print(f"({x1}, {y1})({x2}, {y2})")
        else:
            print(f"({x2}, {y2})({x1}, {y1})")
    else:
        if distance_to_center(x3, y3) <= distance_to_center(x4, y4):
            print(f"({x3}, {y3})({x4}, {y4})")
        else:
            print(f"({x4}, {y4})({x3}, {y3})")

first = float(input())
second = float(input())
third = float(input())
four = float(input())
fifth = float(input())
sixth = float(input())
seventh = float(input())
eighth = float(input())
result = longer_line(first, second, third, four, fifth, sixth, seventh, eighth)
