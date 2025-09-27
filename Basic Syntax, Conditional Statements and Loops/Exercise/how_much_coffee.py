coffee_need = True
coffee_count = 0

while coffee_need:
    stuff_to_do = input()

    if stuff_to_do == 'END':
        game_on = False
        break

    if stuff_to_do.lower() in ('coding', 'cat', 'dog', 'movie'):
        if stuff_to_do.isupper():
            coffee_count += 2
        else:
            coffee_count += 1

if coffee_count > 5:
    print('You need extra sleep')
else:
    print(coffee_count)