
inventory = {}
sold_stuff = 0
while True:
    cmd = input()
    if cmd == "Complete":
        break
    parts = cmd.split()
    if parts[0] == 'Receive':
        quantity = int(parts[1])
        item = parts[2]
        if quantity <= 0:
            continue
        if item not in inventory and quantity > 0:
            inventory[item] = quantity
        elif quantity > 0:
            inventory[item] += quantity

    elif parts[0] == 'Sell':
        quantity = int(parts[1])
        item = parts[2]
        if item not in inventory:
            print(f"You do not have any {item}.")
            continue
        if item in inventory and inventory[item] < quantity:
            sold_quantity = inventory[item]
            sold_stuff += sold_quantity
            print(f"There aren't enough {item}. You sold the last {sold_quantity} of them.")
            del inventory[item]
        else:
            inventory[item] -= quantity
            sold_stuff += quantity
            if inventory[item] <= 0 :
                del inventory[item]
            print(f"You sold {quantity} {item}.")
for k, v in inventory.items():
    print(f"{k}: {v}")
print(f"All sold: {sold_stuff} goods")
