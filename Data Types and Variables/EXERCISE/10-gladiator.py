
lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_breaks = 0
sword_breaks = 0
shield_breaks = 0
armor_breaks = 0

for game in range(1, lost_fights + 1):
    if game % 2 == 0:
        helmet_breaks += 1

    if game % 3 ==0:
        sword_breaks += 1

    if game % 2 == 0 and game % 3==0:
        shield_breaks += 1
        if shield_breaks % 2 == 0:
            armor_breaks += 1



repair_helmet = helmet_price * helmet_breaks
repair_sword = sword_price * sword_breaks
repair_shield = shield_price * shield_breaks
repair_armor = armor_price * armor_breaks

total_money = repair_helmet + repair_shield + repair_armor + repair_sword
print(f"Gladiator expenses: {total_money:.2f} aureus")