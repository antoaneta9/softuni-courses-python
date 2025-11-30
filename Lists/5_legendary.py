game_on = True
dictionary = {
    'shards': 0,
    'fragments': 0,
    'motes': 0,
}
keyword= ''
while game_on:
    text = input().split()
    for i in range(0, len(text), 2):
        material = text[i+1].lower()
        quantity = int(text[i])

        if material not in dictionary:
            dictionary[material] = 0
        dictionary[material] += quantity

        if dictionary['shards'] >= 250:
            dictionary['shards'] -= 250
            keyword = 'Shadowmourne'
            game_on = False
        elif dictionary['motes'] >= 250:
            dictionary['motes'] -= 250
            keyword = 'Dragonwrath'
            game_on = False
        elif dictionary['fragments'] >= 250:
            dictionary['fragments'] -= 250
            keyword = 'Valanyr'
            game_on = False
        if not game_on:
            break
print(f"{keyword} obtained!")
for material, quantity in dictionary.items():
    print(f"{material}: {quantity}")