cart = {}
while True:
    command = input()
    if command == "statistics":
        break

    text = command.split(": ")
    product = text[0]
    quantity = int(text[1])
    if product not in cart:
        cart[product] = 0
        cart[product] += quantity
    else:
        cart[product] += quantity
print('Products in stock:')
for (product, quantity) in cart.items():
    print(f"- {product}: {quantity}")
print(f"Total products: {len(cart.keys())}")
print(f"Total quantity: {sum(cart.values())}")



