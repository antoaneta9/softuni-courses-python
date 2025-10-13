import math
def coordinates(x1, y1, x2, y2):
    first_coord = [x1, y1]
    second_coord = [x2, y2]

    distance_first = (x1 ** 2 + y1 ** 2) ** 0.5
    distance_second = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance_first <= distance_second:
        return first_coord
    else:
        return second_coord

first = float(input())
second = float(input())
third = float(input())
four = float(input())
result = coordinates(math.floor(first), math.floor(second), math.floor(third), math.floor(four))
print(tuple(result))