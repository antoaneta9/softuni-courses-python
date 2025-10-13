rooms = int(input())
chairs_left = 0
game_on = True

for room in range(1, rooms + 1):
    command = input().split(' ')
    chairs = command[0]
    people = int(command[1])

    free_chairs = len(chairs) - people

    if free_chairs < 0:
        print(f"{abs(free_chairs)} more chairs needed in room {room}")
        game_on = False
    else:
        chairs_left += free_chairs

if game_on:
    print(f"Game On, {chairs_left} free chairs left")

