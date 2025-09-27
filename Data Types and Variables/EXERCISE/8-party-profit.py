import math
group_size = int(input())
days = int(input())
coins= 0
each_comp_coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    if day % 5 ==0 and day % 3 == 0:
        coins-=2*group_size
    coins += 50
    coins = coins - (2 * group_size)

    if day % 3 == 0:
        coins = coins - (3 * group_size)

    if day % 5 == 0:
        coins = coins + (20 * group_size)


each_comp_coins = coins // group_size
print(f'{group_size} companions received {math.floor(each_comp_coins)} coins each.')