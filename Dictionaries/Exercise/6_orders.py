cart = {}
total_price = 0
while True:
    text = input()
    if text == 'buy':
        break

    name, price_str, quantity_str = text.split()
    quantity = int(quantity_str)
    price = float(price_str)

    if name not in cart:
        cart[name] = {}
        cart[name]['quantity'] = 0
        cart[name]['price'] = 0
    cart[name]['quantity'] += quantity
    cart[name]['price'] = price

for item in cart:
    total_price = cart[item]['quantity'] * cart[item]['price']
    print(f"{item} -> {total_price:.2f}")









