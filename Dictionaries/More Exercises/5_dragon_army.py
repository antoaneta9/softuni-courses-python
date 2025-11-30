dragons = {}
number_of_dragons = int(input())
for _ in range(number_of_dragons):
    dr_type, name, damage_str, health_str, armor_str = input().split()
    if health_str == 'null':
        health_str = '250'
    if damage_str == 'null':
        damage_str = '45'
    if armor_str == 'null':
        armor_str = '10'

    health = int(health_str)
    damage = int(damage_str)
    armor = int(armor_str)

    if dr_type not in dragons:
        dragons[dr_type] = {}
    dragons[dr_type][name] = (damage, health, armor)

for type_, dragons_by_type in dragons.items():
    dragons[type_] = dict(sorted(dragons_by_type.items()))

for type_, dragons_by_type in dragons.items():
    avg_damage = sum(d[0] for d in dragons_by_type.values()) / len(dragons_by_type)
    avg_health = sum(d[1] for d in dragons_by_type.values()) / len(dragons_by_type)
    avg_armor = sum(d[2] for d in dragons_by_type.values()) / len(dragons_by_type)

    print(f"{type_}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for name, (damage, health, armor) in dragons_by_type.items():
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")