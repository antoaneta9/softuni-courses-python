total_price_no_tax = 0
total_price_with_tax = 0
taxes_amount = 0

total_sum_after_disc = 0
is_special= False
while True:
    command = input()

    if command == 'special':
        is_special = True
        break
    if command == 'regular':
        break

    price = float(command)
    if price <= 0:
        print('Invalid price')
        continue

    total_price_no_tax += price
    taxes_amount += price * 0.20

    total_price_with_tax = taxes_amount + total_price_no_tax
    total_sum_after_disc = total_price_with_tax * 0.90

if total_price_no_tax == 0:
    print('Invalid order!')
elif is_special:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_no_tax:.2f}$\nTaxes: {taxes_amount:.2f}$\n-----------\nTotal price: {total_sum_after_disc:.2f}$")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_no_tax:.2f}$\nTaxes: {taxes_amount:.2f}$\n-----------\nTotal price: {total_price_with_tax:.2f}$")

