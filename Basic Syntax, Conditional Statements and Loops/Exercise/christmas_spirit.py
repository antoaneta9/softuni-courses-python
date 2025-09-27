quantity_decorations = int(input())
days_til_xmas = int(input())

ornament_set_price = 2
tree_skirt = 5
tree_gerland = 3
tree_lights = 15

total_money = 0
points = 0

for day in range(1, days_til_xmas + 1):
    if day % 11 == 0:
        quantity_decorations += 2

    if day % 2 == 0:
        total_money += ornament_set_price * quantity_decorations
        points += 5

    if day % 3 == 0:
        total_money += (tree_skirt + tree_gerland) * quantity_decorations
        points += 13

    if day % 5 == 0:
        total_money += tree_lights * quantity_decorations
        points += 17
        if day % 3 == 0:
            points+=30

    if day % 10 == 0:
        total_money += tree_skirt + tree_gerland + tree_lights
        points -=20


if days_til_xmas % 10 == 0:
    points -=30

print(f'Total cost: {total_money}')
print(f'Total spirit: {points}')