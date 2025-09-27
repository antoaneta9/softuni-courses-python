number_of_lines = int(input())
water_tank = 255
water_collected = 0

for i in range(number_of_lines):
    liters = int(input())
    if water_collected + liters > water_tank:
        print('Insufficient capacity!')

    else:
        water_collected += liters
print(water_collected)