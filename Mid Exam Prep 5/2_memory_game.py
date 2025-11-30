
elements = list(input().split())
moves = 0
while True:
    command = input()

    if command == 'end':
        if len(elements) > 0:
            print('Sorry you lose :(')
            print(*elements)
            break
        break

    moves += 1

    action = command.split(' ')
    index_1 = int(action[0])
    index_2 = int(action[1])

    if index_1 == index_2 or index_1 < 0 or index_2 < 0 or index_1 >= len(elements) or index_2 >= len(elements) or index_2 >= len(elements):
        print('Invalid input! Adding additional elements to the board')
        element = f"-{moves}a"
        middle = len(elements) // 2
        elements.insert(middle, element)
        elements.insert(middle, element)
        continue

    if elements[index_1] == elements[index_2]:
        element_value = elements[index_1]
        print(f"Congrats! You have found matching elements - {element_value}!")
        for index in sorted([index_1, index_2], reverse=True):
            elements.pop(index)

        if not elements:
            print(f'You have won in {moves} turns!')
            break

    else:
        print('Try again!')


