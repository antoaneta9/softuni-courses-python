data = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        break

    if command[0] == 'swap':
        index_1 = int(command[1])
        index_2 = int(command[2])

        data[index_1], data[index_2] = data[index_2], data[index_1]

    elif command[0] == 'multiply':
        index_1 = int(command[1])
        index_2 = int(command[2])

        product = data[index_1] * data[index_2]
        data[index_1] = product

    elif command[0] == 'decrease':
        for el in range(len(data)):
            data[el] -= 1
print(', '.join(map(str, data)))

