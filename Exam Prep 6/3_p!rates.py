cities = {}
while True:
    cmd = input()
    if cmd == 'Sail':
        break
    city, population, gold = cmd.split('||')
    population = int(population)
    gold = int(gold)

    if city in cities:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}


while True:
    cmd = input()
    if cmd == 'End':
        break

    action = cmd.split('=>')
    if action[0] == 'Plunder':
        town = action[1]
        ppl = int(action[2])
        gold = int(action[3])
        if town in cities:
            cities[town]['population'] -= ppl
            cities[town]['gold'] -= gold
            print(f"{town} plundered! {gold} gold stolen, {ppl} citizens killed.")
            if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
                print(f"{town} has been wiped off the map!")
                del cities[town]
    elif action[0] == 'Prosper':
        town = action[1]
        gold = int(action[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
            continue
        if town in cities:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, stats in cities.items():
        print(f"{city} -> Population: {stats['population']} citizens, Gold: {stats['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

