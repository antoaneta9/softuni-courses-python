class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student: str):
        if student not in self.students:
            self.students[student] = []

    def add_grade(self, student: str, grade: float):
        if student in self.students:
            self.students[student].append(grade)
        else:
            print(f"{student} not found in the classroom.")

    def get_average(self, student: str):
        if student in self.students:
            avg = sum(self.students[student]) / len(self.students[student])
            return round(avg, 2)
        return 0.0

    def get_all_averages(self):
        averages = {}
        for student in self.students:
            averages[student] = self.get_average(student)
        return averages

    def top_student(self):
        averages = self.get_all_averages()
        if not averages:
            return "No students in the classroom"
        top_name = max(averages, key=averages.get)
        top_grade = averages[top_name]
        top_students = [name for name, avg in averages.items() if avg == top_grade]
        names = ', '.join(top_students)
        if names:
            return f"Top students: {names} with {top_grade:.2f}"
        return f"Top student: {top_name} with {top_grade:.2f}"

    def __str__(self):
        result = ""
        result += f"Classroom: {self.name}\n"
        for student, grades in self.students.items():
            if grades:
                avg = sum(grades) / len(grades)
            else:
                avg = 0
            result += f"{student} -> {grades} (avg: {avg:.2f})\n"
        return result

room = Classroom("10A")

room.add_student("Ivan")
room.add_student("Maria")
room.add_student("Petar")

room.add_grade("Ivan", 6)
room.add_grade("Ivan", 6)
room.add_grade("Ivan", 5)

room.add_grade("Maria", 6)
room.add_grade("Maria", 6)
room.add_grade("Maria", 5)

room.add_grade("Petar", 4)
room.add_grade("Petar", 5)
room.add_grade("Petar", 6)

print(room)

print("Average for Ivan: ", room.get_average("Ivan"))
print('All averages: ', room.get_all_averages())
print(room.top_student())



