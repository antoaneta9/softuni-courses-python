# course : passowrd
data = {}
while True:
    text = input()
    if text == 'end of courses':
        break
    course, password = text.split(':')
    if course not in data:
        data[course] = password

# data validation
students = {}
while True:
    text = input()
    if text == 'end of submissions':
        break
    course, password, name, points_str = text.split('=>')
    points = int(points_str)
    if course in data and password == data[course]:
        if name not in students:
            students[name] = {}

        if course not in students[name] or students[name][course] < points:
            students[name][course] = points

best_student = max(students, key= lambda x: sum(students[x].values()))
best_points = sum(students[best_student].values())
print(f"Best candidate is {best_student} with total {best_points} points.")
print('Ranking:')
#
# for k, v in students.items():
#     print(f"{k}")
#     for k1, v1 in v.items():
#         print(f"# {k1} -> {v1}")
for key in sorted(students):
    print(key)
    for k, v in sorted(students[key].items(), key=lambda t: -t[1]):
        print(f'# {k} -> {v}')


