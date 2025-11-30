
cars = {}
lines = int(input())
for _ in range(lines):
    car, mileage, fuel = input().split('|')
    cars[car] = {}
    cars[car]['mileage'] = int(mileage)
    cars[car]['fuel'] = int(fuel)

while True:
    cmd = input()
    if cmd == 'Stop':
        break
    parts = cmd.split(' : ')
    if parts[0] == 'Drive':
        car = parts[1]
        distance = int(parts[2])
        fuel = int(parts[3])
        if car in cars:
            if cars[car]['fuel'] >= fuel:
                cars[car]['fuel'] -= fuel
                cars[car]['mileage'] += distance
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car]['mileage'] >= 100000:
                    print(f"Time to sell the {car}.")
                    del cars[car]
            else:
                print(f"Not enough fuel to make that ride")
                continue
    elif parts[0] == 'Refuel':
        car = parts[1]
        refill_amount = int(parts[2])
        if car in cars:
            current_fuel = cars[car]['fuel']
            if current_fuel < 75:
                needed_amount = 75 - current_fuel
                if refill_amount > needed_amount:
                    cars[car]['fuel'] = 75
                    print(f"{car} refueled with {needed_amount} liters")
                else:
                    cars[car]['fuel'] += refill_amount
                    print(f"{car} refueled with {refill_amount} liters")
    elif parts[0] == 'Revert':
        car = parts[1]
        kilometers = int(parts[2])
        if car in cars:
            cars[car]['mileage']-= kilometers
            if cars[car]['mileage'] < 10000:
                cars[car]['mileage'] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

for car, mileage in cars.items():
    print(f"{car} -> {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")

