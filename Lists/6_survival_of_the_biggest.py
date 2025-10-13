str_nums = input()

list_to_nums = str_nums.split()
numbers = []

for i in list_to_nums:
    numbers.append(int(i))

count_to_remove = int(input())

for i in range(count_to_remove):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    for j in range(len(numbers)):
        if numbers[j] == smallest:
            del numbers[j]
            break

for i in range(len(numbers)):
    print(numbers[i], end="")
    if i < len(numbers)-1:
        print(', ', end='')
print()

