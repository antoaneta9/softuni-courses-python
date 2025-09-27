game_on = True

while game_on:
    name = input()

    if name == 'Voldemort':
        print('You must not speak of that name!')
        game_on = False
        break

    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break

    if len(name) < 5:
        print (f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')
