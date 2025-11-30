chest = list(input().split('|'))

while True:
    command = input()
    if command == 'Yohoho!':
        break

    parts = command.split(' ')
    action = parts[0]

    if action == 'Loot':
        items = parts[1:]
        for item in items:
            if item not in chest:
                chest.insert(0, item)
            else:
                continue

    elif action == 'Drop':
        index = int(parts[1])
        if 0 <= index <= len(chest):
            chest.append(chest.pop(index))

        else:
            continue

    elif action == 'Steal':
        count = int(parts[1])
        stolen_stuff = []

        for i in range(count):
            if chest:
                stolen_stuff.insert(0, chest.pop())
        print(', '.join(stolen_stuff))


if len(chest) > 0:
    avg_gain = sum(len(item) for item in chest) / len(chest)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")




