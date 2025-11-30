courses = {}

while True:
    text = input()
    if text == 'end':
        break
    course, student_name = text.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student_name)


for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f"-- {name}")
