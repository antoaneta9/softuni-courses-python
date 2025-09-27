cards = input()
game_over = False

players_a = 11
players_b = 11

red_count_a = set()
red_count_b = set()

if cards:
    cards_splitted = cards.split()
    for card in cards_splitted:
        team, number = card.split('-')
        number = int(number)

        if team == 'A':
            if number not in red_count_a:
                red_count_a.add(number)
                players_a -= 1
        elif team == 'B':
            if number not in red_count_b:
                red_count_b.add(number)
                players_b -= 1

        if players_a < 7 or players_b < 7:
            game_over = True
            break

    print(f'Team A - {players_a}; Team B - {players_b}')
if game_over:
    print('Game was terminated')