health = int(input())
energy = int(input())

total_gold = 0
died = False
while True:
    command = input()

    if command == "Exit":
        print(f"You left the dungeon.")
        print(f"Health: {health}")
        print(f"Energy: {energy}")
        print(f"Gold: {total_gold}")
        break

    parts = command.split(" ")
    action = parts[0]

    if action == 'monster':
        name = parts[1]
        damage = int(parts[2])
        energy_cost = int(parts[3])

        if energy < energy_cost:
            print(f"Not enough energy to fight {name}!")
            continue
        energy -= energy_cost
        if damage >= health:
            print(f"{name} defeated you!")
            died = True
            break
        else:
            health -= damage
            print(f"You slayed {name}!")

    elif action == 'potion':
        amount = int(parts[1])
        if health < 100:
            healed = min(100 - health, amount)
            health += healed
            print(f"You healed for {healed} hp.")
            print(f"Current health: {health} hp.")

    elif action == 'chest':
        amount = int(parts[1])
        total_gold += amount
        print(f"You found {amount} gold.")

    elif action == 'trap':
        damage = int(parts[1])
        energy_loss = int(parts[2])
        health-=damage
        energy-=energy_loss
        if health <= 0:
            print("You died to a trap!")
            died = True
            break
        elif energy <= 0:
            print("You are too exhausted!")
            break
        else:
            print("You survived the trap.")

    elif action == 'rest':
        energy_gain = int(parts[1])
        if energy < 100:
            real_gain = min(100 - energy, energy_gain)
            energy += real_gain
            print(f"You rested and gained {real_gain} energy.")
            print(f"Current energy: {energy}.")

    elif action == 'boss':
        name = parts[1]
        health_needed = int(parts[2])
        energy_needed = int(parts[3])

        if health >= health_needed and energy >= energy_needed:
            print(f"You defeated the boss {name}!")
            print(f"Total gold collected: {total_gold}")
            break
        else:
            print(f"You were not prepared for {name}...")
            break

