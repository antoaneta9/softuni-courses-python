students_book = {}

while True:
    command = input()
    if command == 'end':
        break
    name, subject, grade_ = command.split(' | ')
    grade = float(grade_)

    if name not in students_book:
        students_book[name] = {}
    if subject not in students_book[name]:
        students_book[name][subject] = []
    if subject in students_book[name]:
        students_book[name][subject].append(grade)

for student, subj in students_book.items():
    print(student)
    for subject, grades in subj.items():
        avg = sum(grades) / len(grades)
        print(f"{subject} -> {avg:.2f}")
print(students_book)
print('Overall averages:')
averages = {}
for name, subjects in students_book.items():
    all_grades = [grade for grades in subjects.values() for grade in grades]
    avg = sum(all_grades) / len(all_grades)
    averages[name] = avg
    print(f"{name} -> {avg:.2f}")

top_student = max(averages, key=averages.get)
top_student_grade = averages[top_student]
lowest_student = min(averages, key=averages.get)
lowest_student_grade = averages[lowest_student]
print(f"Top student: {top_student} ({top_student_grade:.2f})")
print(f"Lowest student: {lowest_student} ({lowest_student_grade:.2f})")


