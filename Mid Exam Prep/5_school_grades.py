students = {}
n = int(input())

while n > 0:
    command = input()

    if command == "end":
        if not students:
            print("No data")
        else:
            for name, grades in students.items():
                grades_str = ", ".join(f"{g:.2f}" for g in grades)
                print(f"{name}: {grades_str}")
        break

    parts = command.split(' ')

    if parts[0] == 'add':
        name = parts[1]
        grade = float(parts[2])
        if name not in students:
            students[name] = []
        students[name].append(grade)

    elif parts[0] == 'update':
        name = parts[1]
        grade = float(parts[2])
        new_grade = float(parts[3])
        if name in students and grade in students[name]:
            index = students[name].index(grade)
            students[name][index] = new_grade
        else:
            continue

    elif parts[0] == 'remove':
        name = parts[1]
        grade = float(parts[2])
        if name in students and grade in students[name]:
            students[name].remove(grade)
            if len(students[name]) == 0:
                del students[name]

    elif parts[0] == 'average':
        name = parts[1]
        if name in students:
            avg = sum(students[name])/len(students[name])
            print(f"{name} has an average grade of {avg:.2f}")
        else:
            print(f"Student {name} not found")

    elif parts[0] == 'top':
        if not students:
            print("No students available")
        else:
            top_student = None
            best_avg = -1
            for name, grades in students.items():
                avg = sum(grades)/len(grades)
                if avg > best_avg:
                    best_avg = avg
                    top_student = name
            print(f"Top student: {top_student} with {best_avg:.2f}")
    n-=1
