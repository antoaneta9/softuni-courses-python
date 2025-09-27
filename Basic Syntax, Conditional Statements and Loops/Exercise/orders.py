number_of_orders = int(input())
total_price = 0.0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule > 100.00 or price_per_capsule < 0.01:
        continue

    if days < 0 or days > 31:
        continue

    if capsules_needed_per_day < 0 or capsules_needed_per_day > 2000:
        continue

    order_price = price_per_capsule * days * capsules_needed_per_day
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price += order_price
print(f'Total: ${total_price:.2f}')