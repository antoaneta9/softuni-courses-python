
student_book = {}
while True:
    text = input()
    if text == 'end':
        break

    name, points_str = text.split(' -> ')
    points = int(points_str)
    if name not in student_book:
        student_book[name] = []
    student_book[name].append(points)

# SUM POINTS FOR EACH STUDENT
for k, v in student_book.items():
    print(f'{k} -> {sum(v)}')

# BEST STUDENT
best_name = max(student_book, key=lambda x: sum(student_book[x]))
best_points = sum(student_book[best_name])
print(f'Best student is {best_name} with total {best_points} points.')


