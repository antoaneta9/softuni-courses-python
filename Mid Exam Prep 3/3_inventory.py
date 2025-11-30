items = list(input().split(', '))

while True:
    command = input()
    if command == "Craft!":
        break

    parts = command.split(' - ')
    action = parts[0]

    if action == 'Collect':
        item = parts[1]
        if item not in items:
            items.append(item)
        else:
            continue

    elif action == 'Drop':
        item = parts[1]
        if item not in items:
            continue
        else:
            items.remove(item)

    elif action =='Combine Items':
        items__ = parts[1].split(':')
        old_item = items__[0]
        new_item = items__[1]
        if old_item in items:
            index_old_item = items.index(old_item)
            items.insert(index_old_item + 1, new_item)
        else:
            continue

    elif action == 'Renew':
        item = parts[1]
        if item in items:
            items.remove(item)
            items.append(item)
        else:
            continue

print(', '.join(items))