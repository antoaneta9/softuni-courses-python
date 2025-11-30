import random
balance = float(input())
reputation = int(input())
technology_level = int(input())

ships = []
resources = {"ore": 0, "food": 0, "fuel": 0, "crystals": 0}
while True:
    command = input()
    if command == 'Shutdown':
        if reputation < 0:
            print("You have been blacklisted! Game Over.")
        else:
            print("Hub Status:")
            print(f"Balance: {balance:.2f}")
            print(f"Reputation: {reputation}")
            print(f"Technology: {technology_level}")
            print(f"Resources: ore={resources['ore']}, food={resources['food']}, fuel={resources['fuel']}, crystals={resources['crystals']}")
            print(f"Ships count: {len(ships)}")
        break

    parts = command.split(' ')
    action = parts[0]
    if action == 'BuyResource':
        type_of_unit = parts[1]
        quantity = int(parts[2])
        price_per_unit = float(parts[3])
        if type_of_unit not in resources:
            continue
        else:
            total_price = price_per_unit * quantity
            if balance < total_price:
                print("Insufficient funds!")
            else:
                balance -= total_price
                resources[type_of_unit] += quantity

    elif action == 'SellResource':
        type_of_unit = parts[1]
        quantity = int(parts[2])
        price_per_unit = float(parts[3])
        if type_of_unit not in resources:
            continue
        else:
            if resources[type_of_unit] < quantity:
                print(f"Not enough {type_of_unit}!")
            else:
                resources[type_of_unit] -= quantity
                balance += quantity * price_per_unit

    elif action == 'HireShip':
        name = parts[1]
        crew = int(parts[2])
        capacity = int(parts[3])
        fuel_usage = int(parts[4])
        price_to_rent = crew * 100
        if balance < price_to_rent:
            print("Cannot afford ship!")
        else:
            balance -= price_to_rent
            ship = {
                "name": name,
                "crew": crew,
                "capacity": capacity,
                "fuel_usage": fuel_usage
            }
            ships.append(ship)

    elif action == 'FireShip':
        name = parts[1]
        found = False
        for ship in ships:
            if ship["name"] == name:
                ships.remove(ship)
                found = True
                print(f"{name} has been dismissed.")
                break
        if not found:
            print(f"{ship['name']} not found!")

    elif action == "Mission":
        ship_name = parts[1]
        mission_type = parts[2]
        if mission_type == 'mining':
            fuel_needed = 0
            ship = None
            for s in ships:
                if s["name"] == ship_name:
                    ship = s
                    break
            if ship is None:
                print("Ship not found!")
                continue

            fuel_needed = ship["fuel_usage"] * 10
            if resources['fuel'] < fuel_needed:
                print('Not enough fuel!')
            else:
                resources['fuel'] -= fuel_needed
                reputation +=1
                R = random.randint(20, 50)
                resources["ore"] += R
                print("Mining mission successful!")
        elif mission_type == 'trading':
            fuel_needed = 0
            ship = None
            for s in ships:
                if s["name"] == ship_name:
                    ship = s
                    break
            if ship is None:
                print("Ship not found!")
                continue
            fuel_needed = ship["fuel_usage"] * 5
            if resources['fuel'] < fuel_needed:
                print('Not enough fuel!')
            else:
                resources['fuel'] -= fuel_needed
                if resources['food'] >= 10:
                    resources['food'] -= 10
                    P = random.randint(20, 50)
                    balance += P
                    reputation += 2
                    print('Trading mission completed!')
        elif mission_type == 'exploration':
            fuel_needed = 0
            ship = None
            for s in ships:
                if s["name"] == ship_name:
                    ship = s
                    break
            if ship is None:
                print("Ship not found!")
                continue
            fuel_needed = ship["fuel_usage"] * 15
            if resources['fuel'] < fuel_needed:
                print('Not enough fuel!')
            else:
                resources['fuel'] -= fuel_needed
                if random.random() < 0.5:
                    c = random.randint(5, 15)
                    resources['crystals'] += c
                    reputation += 5
                    print("Exploration result: success")
                else:
                    ships.remove(ship)
                    reputation -= 10
                    print("Exploration result: failure")

    elif action == 'Research':
        points = int(parts[1])
        price = points * 200
        if balance < price:
            print("Not enough money for research!")
        else:
            balance -= price
            technology_level += points
            if technology_level >= 50:
                reputation += 20

    elif action == 'PayCrew':
        total_cost = 0
        for ship in ships:
            total_cost += ship["crew"] * 50

        if balance >= total_cost:
            balance -= total_cost
            reputation += len(ships)
            print("Crew has been paid.")
        else:
            reputation -= 10
            print("Could not pay crew!")


    elif action == 'Tax':
        tax_ = balance * 0.10
        balance -= tax_
        reputation -= 5

    elif action == 'Status':
        print(f"Balance: {balance}")
        print(f"Reputation: {reputation}")
        print(f"Technology: {technology_level}")
        print(f"Resources: ore={resources['ore']}, food={resources['food']}, fuel={resources['fuel']}, crystals={resources['crystals']}")
        if ships:
            print("Ships:")
            print("- Name | Crew | Capacity | FuelUsage")
            for ship in ships:
                print(f"- {ship['name']} | {ship['crew']} | {ship['capacity']} | {ship['fuel_usage']}")
        else:
            print("Ships: None")






