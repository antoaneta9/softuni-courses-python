#part one: storing players data
players_data = {}
while True:
    text = input()
    if text == 'Season end':
        break

    if ' -> ' in text:
        player_name, position, skill_ =text.split(' -> ')
        skill = int(skill_)
        if player_name not in players_data:
            players_data[player_name] = {}
        if position not in players_data[player_name]:
            players_data[player_name][position] = skill
        else:
            if players_data[player_name][position] < skill:
                players_data[player_name][position] = skill
    elif ' vs ' in text:
        player_1, player_2 = text.split(' vs ')
        if player_1 in players_data and player_2 in players_data:
            common_positions = set(players_data[player_1].keys()) & set(players_data[player_2].keys())
            if common_positions:
                total_1 = sum(players_data[player_1].values())
                total_2 = sum(players_data[player_2].values())
                if total_1 > total_2:
                    del players_data[player_2]
                elif total_2 > total_1:
                    del players_data[player_1]
#
# part two: sorting and printing

player_totals = []
for player, positions in players_data.items():
    total = sum(positions.values())
    player_totals.append((player, total))

sorted_players = sorted(player_totals, key=lambda x: (-x[1], x[0]))
for player, total in sorted_players:
    print(f"{player}: {total} skill")
    sorted_positions = sorted(players_data[player].items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")



