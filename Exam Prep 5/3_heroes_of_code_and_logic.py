
heroes = {}
lines = int(input())
for _ in range(lines):
    name, hit_points, mana_points = input().split()
    heroes[name] = {
        'hit_points': int(hit_points),
        'mana_points': int(mana_points)
    }

while True:
    cmd = input()
    if cmd == 'End':
        break
    parts = cmd.split(' - ')
    if parts[0] == 'CastSpell':
        name = parts[1]
        mana_needed = int(parts[2])
        spell_name = parts[3]

        if heroes[name]['mana_points'] >= mana_needed:
            heroes[name]['mana_points'] -= mana_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mana_points']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif parts[0] == 'TakeDamage':
        name = parts[1]
        damage = int(parts[2])
        attacker = parts[3]

        heroes[name]['hit_points'] -= damage
        if heroes[name]['hit_points'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hit_points']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
    elif parts[0] == 'Recharge':
        name = parts[1]
        amount = int(parts[2])
        current_mp = heroes[name]['mana_points']
        if current_mp <= 200:
            needed_mp = 200 - current_mp
            if amount >= needed_mp:
                heroes[name]['mana_points'] = 200
                print(f"{name} recharged for {needed_mp} MP!")
            else:
                heroes[name]['mana_points'] += amount
                print(f"{name} recharged for {amount} MP!")
    elif parts[0] == 'Heal':
        name = parts[1]
        amount = int(parts[2])

        current_hp = heroes[name]['hit_points']
        if current_hp <= 100:
            needed_hp = 100 - current_hp
            if amount >= needed_hp:
                heroes[name]['hit_points'] = 100
                print(f"{name} healed for {needed_hp} HP!")
            else:
                heroes[name]['hit_points'] += amount
                print(f"{name} healed for {amount} HP!")

for name, stats in heroes.items():
    print(f"{name}")
    print(f"  HP: {stats['hit_points']}")
    print(f"  MP: {stats['mana_points']}")
