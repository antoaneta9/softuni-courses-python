students_book = {}
while True:
    text = input()
    if text == 'end':
        break

    name, subj, points_str = text.split(' -> ')
    points = int(points_str)

    if name not in students_book:
        students_book[name] = {}

    if subj not in students_book[name]:
        students_book[name][subj] = points
    else:
        if students_book[name][subj] < points:
            students_book[name][subj] = points

for k, v in students_book.items():
    print(k)
    for k1, v1 in v.items():
        print(f"# {k1} -> {v1}")