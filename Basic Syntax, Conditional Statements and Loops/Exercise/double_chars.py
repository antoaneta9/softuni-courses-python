game_on = True

while game_on:
    string = input()

    if string == 'SoftUni':
        continue


    if string == 'End':
        game_on = False
        break

    result = ''
    for char in string:
        result += char * 2

    print(result)


