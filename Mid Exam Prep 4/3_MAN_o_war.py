status_pirate_ship = list(map(int, input().split('>')))
status_warship = list(map(int, input().split('>')))
max_health = int(input())

won = False
lost = False

while True:
    command = input()
    if command == 'Retire':
        break

    parts = command.split(' ')
    action = parts[0]
    if action == 'Fire':
        index_attack = int(parts[1])
        damage = int(parts[2])
        if 0 <= index_attack < len(status_warship):
            status_warship[index_attack] -= damage
            if status_warship[index_attack] <= 0:
                print('You won! The enemy ship has sunken.')
                won = True
                break
        else:
            continue

    elif action == 'Defend':
        start = int(parts[1])
        end = int(parts[2])
        damage = int(parts[3])
        if 0 <= start < len(status_pirate_ship) and 0 <= end < len(status_pirate_ship):
            for i in range(start, end + 1):
                status_pirate_ship[i] -= damage
                if status_pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost = True
                    break
                if lost:
                    break

        else:
            continue

    elif action == 'Repair':
        index = int(parts[1])
        health = int(parts[2])
        if 0 <= index < len(status_pirate_ship):
            status_pirate_ship[index] = min(status_pirate_ship[index] + health, max_health)
        else:
            continue

    elif action == 'Status':
        lower_health = max_health * 0.2
        count = 0
        for section in status_pirate_ship:
            if section < lower_health:
                count += 1
        print(f"{count} sections need repair.")

if not won and not lost:
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_warship)}")
