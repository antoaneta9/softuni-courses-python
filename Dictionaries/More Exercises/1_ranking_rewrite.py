contests = {}

while True:
    command = input()
    if command == 'end of contests':
        break

    contest, password = command.split(':')
    if contest not in contests:
        contests[contest] = password

allowed_students = {}
while True:
    command = input()
    if command == 'end of submissions':
        break

    contest_, password_, username, points_st = command.split('=>')
    points = int(points_st)
    if contest_ in contests and password_ == contests[contest_]:
        if username not in allowed_students:
            allowed_students[username] = {}

        if contest_ not in allowed_students[username] or allowed_students[username][contest_] < points:
            allowed_students[username][contest_] = points
top_name = max(allowed_students, key=lambda x: sum(allowed_students[x].values()))
top_points = sum(allowed_students[top_name].values())

print(f"Best candidate is {top_name} with total {top_points} points.")
print('Ranking:')
for key, value in sorted(allowed_students.items()):
    print(f"{key}")
    for k, v in sorted(value.items(), key=lambda x: -x[1]):
        print(f"#  {k} -> {v}")
