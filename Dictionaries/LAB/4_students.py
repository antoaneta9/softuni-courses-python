students = {}
course_to_find = ''

while True:
    command = input()
    if ':' not in command:
        course_to_find = command.lower()
        break

    name, student_id, subject = command.split(':')
    subject = subject.lower().replace(' ', '_')
    students[(name, student_id)] = subject

for (name, student_id), subject in students.items():
    if subject == course_to_find:
        print(f"{name} - {student_id}")

"""
    - The key (name, student_id) is a tuple — immutable, so valid as a dict key.
    - Lists and dicts can't be keys because they're mutable (unhashable).
    Alternatives: nested dict: students[name] = {'id': students_id, 'subject': subject}
                  list of dicts: (but not compatible with this LAB)
"""