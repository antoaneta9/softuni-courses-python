employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
students_count = int(input())

students_answered_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
# break every 4th hour but it is the only break so they work 8hours
hours_passed = 0

while students_count > 0:
    hours_passed += 1
    if hours_passed % 4 == 0:
        continue
    students_count -= students_answered_per_hour


print(f"Time needed: {hours_passed}h.")
