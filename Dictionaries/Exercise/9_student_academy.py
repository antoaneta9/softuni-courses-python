lines = int(input())
student_book = {}

for j in range(lines):
    name = input()
    grade = float(input())
    if name not in student_book:
        student_book[name] = []
    student_book[name].append(grade)

for name, grades in student_book.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{name} -> {average:.2f}")
