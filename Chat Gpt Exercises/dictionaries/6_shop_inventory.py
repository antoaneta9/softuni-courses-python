
inventory = {}
while True:
    command = input()
    if command == "stop":
        break

    food, count_str = command.split()
    count = int(count_str)

    if food not in inventory:
        inventory[food] = count
    elif food in inventory:
        inventory[food] += count
print(inventory)
