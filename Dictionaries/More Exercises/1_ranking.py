# LOGIN DATA

data_login = {}
while True:
    text = input()
    if text == 'end of contests':
        break

    contest,password = text.split(':')
    if contest not in data_login:
        data_login[contest] = password
# print(data_login)

# STUDENTS DATA
students_data = {}
while True:
    text = input()
    if text == 'end of submissions':
        break
    course, password, name, points_str = text.split('=>')
    points = int(points_str)
    if course in data_login and password == data_login[course]:
        if name not in students_data:
            students_data[name] = {}

        if course not in students_data[name] or students_data[name][course] < points:
            students_data[name][course] = points

# BEST STUDENT
best_student = max(students_data, key=lambda x: sum(students_data[x].values()))
best_points = sum(students_data[best_student].values())

# FORMATTING
print(f"Best candidate is {best_student} with total {best_points} points.")
print('Ranking:')
for key in sorted(students_data):
    print(key)
    for k, v in sorted(students_data[key].items(), key=lambda t: -t[1]):
        print(f'# {k} -> {v}')