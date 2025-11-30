departments = {}

while True:
    employee = input()
    if employee == 'end':
        break
    name, salary_, department = employee.split('-')
    salary = float(salary_)

    if department not in departments:
        departments[department] = {}

    departments[department][name] = salary

best_dep = ""
best_avg = 0

for dep, workers in departments.items():
    avg = sum(workers.values()) / len(workers)
    if avg > best_avg:
        best_avg = avg
        best_dep = dep

print(f"Highest Average Salary: {best_dep}")

for name, salary in sorted(departments[best_dep].items(), key=lambda x: -x[1]):
    print(f"{name} {salary:.2f}")


