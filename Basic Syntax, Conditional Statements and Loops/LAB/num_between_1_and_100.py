game_on = True
while game_on:
    number = float(input())
    if number >= 1 and number <= 100:
        print(f'The number {number} is between 1 and 100')
        game_on = False
        break
    else:
        continue
