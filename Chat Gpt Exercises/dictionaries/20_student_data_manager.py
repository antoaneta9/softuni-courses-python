students_count = int(input())
students = {}

for _ in range(students_count):
    name, grades_str = input().split(":")
    grades = [float(g) for g in grades_str.split(",")]
    students[name] = {"grades": grades, "comments": []}
# print(students)

def average(name):
    if name not in students:
        print(f"No student named {name}.")
        return
    grades = students[name]["grades"]
    avg = sum(grades) / len(grades)
    print(f"Average score for {name}: {avg:.2f}")
    return avg

def top(count):
    step = 1
    count = int(count)
    sorted_students = sorted(students.items(), key=lambda x: sum(x[1]['grades']) / len(x[1]['grades']), reverse=True)
    print(f"Top {count} students:")
    for name, data in sorted_students[:count]:
        avg = average(name)
        print(f"{step}. {name}: {avg:.2f}")
        step += 1

def add_comment(student_name, text):
    if student_name in students:
        students[student_name]['comments'].append(comment)
        print(f"Added comment for {name}. ({comment})")
    else:
        print(f'No student with that {name}.')

def info(name):
    if name not in students:
        print(f"No student called {name}")
    data = students[name]
    avg = sum(data["grades"]) / len(data["grades"])
    print(f"Info for {name}:")
    print(f"\tAverage grade for {name}: {avg:.2f}")
    if data["comments"]:
        print(f"\tComments for {name}:")
        for comment in data["comments"]:
            print(f"\t----> {comment} <----")
    else:
        print(f"No comments for {name}")

def search(word):
    word = word.lower()
    is_found = False
    print(f"Searching for comments with the word '{word}':")
    for name, data in students.items():
        for comment in data["comments"]:
            if word in comment.lower():
                print(f"  {name}: {comment}")
                is_found = True
    if not is_found:
        print(f"No comments found containing '{word}'.")

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    cmd = parts[0]
    if cmd == 'average':
        average(parts[1])
    elif cmd == "top":
        top(parts[1])
    elif cmd == 'comment':
        name = parts[1]
        comment = ' '.join(parts[2:])
        if len(comment) > 2:
            add_comment(name, comment)
        else:
            pass
    elif cmd == "info":
        info(parts[1])
    elif cmd == "search":
        search(parts[1])





