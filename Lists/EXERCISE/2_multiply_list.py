factor = int(input())
count = int(input())
list_of_numbers = []


for n in range(1, count + 1):
    total = n * factor
    list_of_numbers.append(total)
print(list_of_numbers)


