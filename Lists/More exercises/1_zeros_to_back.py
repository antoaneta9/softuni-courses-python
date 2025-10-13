numbers = list(map(int, input().split(', ')))
zeros = []
for number in numbers:
    if 0 in numbers:
        zeros.append(0)
        numbers.remove(0)
# print(numbers)
# print(zeros)
new_list = numbers + zeros
print(new_list)
