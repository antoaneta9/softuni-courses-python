initial_health = 100
initial_bitcoins = 0

dungeon_rooms = list(input().split('|'))
room_count = 0
for room in dungeon_rooms:
    command, integer = room.split()
    integer = int(integer)
    room_count += 1
    if command == 'potion':
        healed = integer
        if initial_health < 100:
            healed = min(100 - initial_health, healed)
            initial_health += healed
            print(f"You healed for {healed} hp.")
            print(f"Current health: {initial_health} hp.")

    elif command == 'chest':
        initial_bitcoins += integer
        print(f"You found {integer} bitcoins.")

    else:
        initial_health-=integer
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break

else:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")

