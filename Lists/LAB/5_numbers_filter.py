lines = int(input())
numbers = []
filtered = []

for i in range(1, lines + 1):
    curr_num = int(input())
    numbers.append(curr_num)

command = input()

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif command == 'odd':
    for num in numbers:
        if num % 2 == 1:
            filtered.append(num)
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered.append(num)
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered.append(num)

print(filtered)