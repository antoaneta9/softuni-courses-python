planets_and_astronauts = {}
astronauts_quantity = int(input())

for _ in range(astronauts_quantity):
    text = input()
    astronaut_name, planet, resource_data = text.split(' -> ')
    resource_list = resource_data.split(',')
    resource_dict = {}
    for resource in resource_list:
        resource_name, resource_value = resource.split(':')
        resource_dict[resource_name] = int(resource_value)

    planets_and_astronauts[astronaut_name] = {
        'planet': planet,
        'resources': resource_dict
    }
print(planets_and_astronauts)

while True:
    text = input().split()
    cmd = text[0]
    if cmd == 'end':
        print(planets_and_astronauts)
        break


    if cmd == 'explore':
        name = text[1]
        new_planet = text[2]
        if name in planets_and_astronauts.keys() and new_planet != planets_and_astronauts[name]['planet']:
            planets_and_astronauts[name]['planet'] = new_planet
            print(f"{name} is exploring {new_planet}")

    elif cmd == 'collect':
        name = text[1]
        resource = text[2]
        amount = int(text[3])
        if resource in planets_and_astronauts[name]['resources']:
            planets_and_astronauts[name]['resources'][resource] += int(amount)
            print(f"{name} is collecting {amount} from {resource}")
        elif resource not in planets_and_astronauts[name]['resources']:
            planets_and_astronauts[name]['resources'][resource] = int(amount)
            print(f"{name} is adding {amount} of {resource} to his bag.")

    elif cmd == 'status':
        name = text[1]
        if name in planets_and_astronauts:
            print(f"The astronaut '{name}' is on planet {planets_and_astronauts[name]['planet']}.")
            print(f'{name} has resources of: ')
            for k, v in planets_and_astronauts[name]['resources'].items():
                print(f"\t-{k}: {v} quantity.")

    elif cmd == 'report':
        print('=== Mission Report ===')
        for k, v in planets_and_astronauts.items():
            print(f'{k} ({planets_and_astronauts[k]["planet"]}): ')
            for resource_name, amount in planets_and_astronauts[k]['resources'].items():
                print(f'\t{resource_name}: {amount}')
        print('-------------------------')
        total_resources=0
        for key, value in planets_and_astronauts.items():
            for resource_name, amount in planets_and_astronauts[key]['resources'].items():
                total_resources += amount
        print(f"Total resources: {total_resources}")
        active_planets = []
        for key, value in planets_and_astronauts.items():
            for k, v in value.items():
                if k == 'planet':
                    active_planets.append(v)
        print(f"Active planets: {len(active_planets)}")
        top_collector = ''
        top_amount = 0
        for key, value in planets_and_astronauts.items():
            total = sum(value['resources'].values())
            if total > top_amount:
                top_amount = total
                top_collector = key
        print(f"Top collector is {top_collector} with {top_amount} total resources.")
        print('=========================')





