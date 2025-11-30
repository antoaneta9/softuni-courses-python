budget = int(input())

while True:
    command = input()
    if command =='End':
        print(f'Money left: {budget:.2f}')

        break

    action = command.split(' ')
    product = action[0]
    price = int(action[1])

    if price <= budget:
        budget -= price
        print(f"Bought {product}")
    else:
        print(f"Too expensive!")
        continue

    if budget == 0:
        print('You bought everything!')
        break