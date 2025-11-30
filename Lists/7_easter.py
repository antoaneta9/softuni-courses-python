
gifts_to_buy = input().split(' ')

while True:
    cmd = input()
    if cmd == 'No Money':
        break

    parts = cmd.split(' ')
    if parts[0] == 'OutOfStock':
        gift = parts[1]
        for i in range(len(gifts_to_buy)):
            if gifts_to_buy[i] == gift:
                gifts_to_buy[i] = 'None'
    elif parts[0] == 'Required':
        gift, index = parts[1], int(parts[2])
        if 0 <= index < len(gifts_to_buy):
            gifts_to_buy.pop(index)
            gifts_to_buy.insert(index, gift)
        else:
            continue
    elif parts[0] == 'JustInCase':
        gift = parts[1]
        if gifts_to_buy:
            gifts_to_buy.pop()
            gifts_to_buy.append(gift)
if gifts_to_buy:
    for gift in gifts_to_buy:
        if gift == 'None':
            continue
        else:
            print(gift, end=' ')

