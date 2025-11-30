travel_route = input().split('||')
fuel = int(input())
ammunition = int(input())

for route in travel_route:
    parts = route.split()
    command = parts[0]
    if command == "Travel":
        light_years = int(parts[1])
        if fuel >= light_years:
            fuel-=light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print(f"Mission failed.")
            break

    elif command == 'Enemy':
        enemy_armour = int(parts[1])
        if ammunition >= enemy_armour:
            needed_ammunition = enemy_armour
            ammunition -= needed_ammunition
            print(f"An enemy with {enemy_armour} armour is defeated.")
        else:
            if fuel >= enemy_armour:
                fuel -= enemy_armour
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            else:
                print(f"Mission failed.")
                break

    elif command == 'Repair':
        amount = int(parts[1])
        fuel+=amount
        ammunition += amount * 2
        print(f"Ammunitions added: {amount * 2}.")
        print(f"Fuel added: {amount}.")

    elif command == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break

