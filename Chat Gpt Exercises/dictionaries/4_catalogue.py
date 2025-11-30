fridge = {}
while True:
    text = input()
    if text == 'stop':
        break

    food, category = text.split(':')
    if category not in fridge:
        fridge[category] = []
        fridge[category].append(food)
    elif category in fridge:
        fridge[category].append(food)

print(fridge)



