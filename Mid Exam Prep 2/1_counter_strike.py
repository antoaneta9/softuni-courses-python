full_energy = int(input())
won_battles = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f"Won battles: {won_battles}. Energy left: {full_energy}")
        break

    distance_to_int = int(command)

    if full_energy < distance_to_int:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {full_energy} energy")
        break

    full_energy -= distance_to_int
    won_battles += 1

    if won_battles % 3 == 0:
        full_energy += won_battles

