gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    parts = command.split()

    if parts[0] == "OutOfStock":
        gift_to_remove = parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif parts[0] == "Required":
        new_gift = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = new_gift

    elif parts[0] == "JustInCase":
        new_gift = parts[1]
        gifts[-1] = new_gift

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
print()