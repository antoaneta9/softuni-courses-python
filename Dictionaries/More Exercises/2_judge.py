students_data = {}
contest_order = []
user_order = {}
user_counter = 0

while True:
    text = input()
    if text == 'no more time':
        break
    username, contest, points_ = text.split(' -> ')
    points = int(points_)

    if contest not in contest_order:
        contest_order.append(contest)

    if username not in students_data:
        students_data[username] = {}
        user_order[username] = user_counter
        user_counter += 1

    if contest not in students_data[username]:
        students_data[username][contest] = points
    else:
        if students_data[username][contest] < points:
            students_data[username][contest] = points

contests = {}
for user, user_contest in students_data.items():
    for contest, pts in user_contest.items():
        if contest not in contests:
            contests[contest] = {}
        contests[contest][user] = pts

for contest in contest_order:
    participants = contests[contest]
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(
        participants.items(),
        key=lambda t: (-t[1], t[0], user_order[t[0]])
    )
    for count, (username, pts) in enumerate(sorted_participants, start=1):
        print(f"{count}. {username} <::> {pts}")

individuals = {}
for user, contests_ in students_data.items():
    total = sum(contests_.values())
    individuals[user] = total

sorted_individuals = sorted(
    individuals.items(),
    key=lambda x: (-x[1], x[0], user_order[x[0]])
)

print('Individual standings:')
for count, (person, points) in enumerate(sorted_individuals, start=1):
    print(f"{count}. {person} -> {points}")





