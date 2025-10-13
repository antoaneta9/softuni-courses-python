def smallest_of_three():
    a = int(input())
    b = int(input())
    c = int(input())
    list_of_numbers = [a, b, c]
    smallest = min(list_of_numbers)
    return smallest
result = smallest_of_three()
print(result)
