students = int(input())
total_num_lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_attendance = 0
lst_of_attendance = []
for student in range(students):
    attendance = int(input())
    lst_of_attendance.append(attendance)
    if attendance > max_attendance:
        max_attendance = max(lst_of_attendance)
        total_bonus = (max_attendance / total_num_lectures) * (5 + additional_bonus)


print(f"Max bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")


