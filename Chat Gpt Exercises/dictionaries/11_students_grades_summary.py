
students_book = {}
lines = int(input())
for line in range(lines):
    text = input()
    name, grade_str = text.split()
    grade = float(grade_str)
    if name not in students_book:
        students_book[name] = []
    students_book[name].append(grade)

sorted_students_book = sorted(students_book.items(), key=lambda x: x[0])
for k, v in sorted_students_book:
    average = sum(v) / len(v)
    print(f"{k} -> {average:.2f}")

