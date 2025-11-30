plants = {}

lines = int(input())
for _ in range(lines):
    plant, rarity_ = input().split('<->')
    rarity = int(rarity_)

    plants[plant] = {
    'rarity': rarity,
    'ratings': [],
    }

while True:
    cmd = input()
    if cmd == 'Exhibition':
        break

    action, info = cmd.split(': ')
    if action == 'Rate':
        plant, rating_ = info.split(' - ')
        rating = int(rating_)
        if plant in plants:
            plants[plant]['ratings'].append(rating)
        else:
            print('error')

    elif action == 'Update':
        plant, new_rarity_ = info.split(' - ')
        new_rarity = int(new_rarity_)
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print('error')

    elif action == 'Reset':
        plant = info
        if plant in plants:
            plants[plant]['ratings'].clear()
        else:
            print('error')


print("Plants for the exhibition:")
for plant, data in plants.items():
    if data['ratings']:
        avg = sum(data['ratings']) / len(data['ratings'])
    else:
        avg = 0
    print(f"- {plant}; Rarity: {data['rarity']}; Ratings: {avg:.2f}")