water_price = 1.00
energy_price = 1.50
protein_price = 2.00
total_price = 0

while True:
    command = input()
    if command =='End':
        print(f'Total: {total_price:.2f} lv.')
        break

    parts = command.split(' ')
    product = parts[0].lower()
    count = float(parts[1])

    if count < 1:
        print('Invalid order!')
        continue

    if product == 'water':
        total_price += water_price * count
    elif product == 'energy':
        total_price += energy_price * count
    elif product == 'protein':
        total_price += protein_price * count

    if total_price > 200:
        print(f"Enough! You've reached the limit.\nTotal: {total_price:.2f} lv.")
        break

    if total_price > 100:
        total_price *= 0.90





