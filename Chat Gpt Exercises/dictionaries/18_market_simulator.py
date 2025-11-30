lines = int(input())
products = {}
sold_products = {}
for _ in range(lines):
    name, price_, quantity_ = input().split(':')
    price = float(price_)
    quantity = int(quantity_)
    if name not in products:
        products[name] = {}
    products[name]['price'] = price
    products[name]['quantity'] = quantity

total_price = 0
while True:
    command = input().split()
    cmd = command[0]

    if cmd == 'End':
        break

    if cmd == 'Buy':
        name = command[1]
        quantity = int(command[2])
        if name in products and quantity <= products[name]['quantity']:
# sold_products.get(name, 0) + quantity [and not just ... = quantity, bc if products is bought more than once it will just overwrite its quantity ]
            sold_products[name] = sold_products.get(name, 0) + quantity
            total_price += products[name]['price'] * quantity
            products[name]['quantity'] -= quantity
        elif name in products and quantity > products[name]['quantity']:
            print(f'Not enough quantity of {name} in stock')
        else:
            print(f"{name} not in stock.")

    elif cmd == 'Restock':
        name = command[1]
        quantity = int(command[2])
        if name in products:
            products[name]['quantity'] += quantity
        else:
            print(f"{name} not in stock.")

    elif cmd == 'ChangePrice':
        name = command[1]
        new_price = float(command[2])
        if name in products:
            products[name]['price'] = new_price
        else:
            print(f"{name} not in stock.")

    elif cmd == 'Report':
        print(f"Total price: {total_price}")
        most_sold = max(sold_products, key=sold_products.get)
        count = 0
        for key, value in sold_products.items():
            if key == most_sold:
                count = value
        print(f"Most sold product: {most_sold}({count})")

    elif cmd == 'Status':
        print('<-------------------------->')
        print(f"Current stuff in the shop: ")
        for key, value in products.items():
            print(f"{key}:")
            for k, v in value.items():
                print(f'\t- {k}: {v}')
        print('<-------------------------->')

# TO IMPROVE ADD "DELETE" AND "ADD" CMD
