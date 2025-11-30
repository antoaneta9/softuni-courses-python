import re
pattern = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
cmd = input()
bought_furniture = []
total = 0
while cmd != 'Purchase':
    matches = re.search(pattern, cmd, re.IGNORECASE)
    if matches:
        name, price, quantity = matches.groups()
        bought_furniture.append(name)
        total += float(price) * int(quantity)
    cmd = input()
print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total:.2f}")

