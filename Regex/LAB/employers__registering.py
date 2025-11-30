import re

name_regex = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
age_regex = r'^\d{2}$'
email_regex = r'^[a-z0-9]+[a-z0-9._-]*@[a-z0-9-]+\.[a-z.]{2,}$'
position_regex = r'^(developer|manager|designer|analyst|intern)$'
salary_regex = r'^\d+(\.\d{1,2})?$'
employee_id_regex = r'^EMP-\d{5}$'

valid_employees = {}
invalid_employees = {}

while True:
    command = input()
    if command == 'end':
        break
    errors = []
    name, age, email, position, salary, employee_id = command.split(' | ')
    if not re.match(name_regex, name):
        errors.append('Invalid name')
    if not re.match(age_regex, age):
        errors.append('Invalid age')
    if not re.match(email_regex, email):
        errors.append('Invalid email')
    if not re.match(position_regex, position):
        errors.append('Invalid position')
    if not re.match(salary_regex, salary):
        errors.append('Invalid salary')
    if not re.match(employee_id_regex, employee_id):
        errors.append('Invalid employee id')
    # IF REGEX IS PASSED MORE VALIDATION APPLIED
    if not errors:
        age = int(age)
        if not (18 <= age <= 65):
            errors.append('Invalid age range')
        salary = float(salary)
        if position == 'intern' and salary > 1500:
            errors.append('Salary is too high for intern')
        elif position == 'manager' and salary < 3000:
            errors.append('Salary is too low for manager')
        elif position == 'developer' and salary < 2000:
            errors.append('Salary is too low for developer')
    # FINAL DECISION
    if errors:
        invalid_employees[employee_id] = errors
    else:
        if employee_id in valid_employees and valid_employees[employee_id]['salary'] > salary:
                valid_employees[employee_id]['salary'] = salary
        else:
            valid_employees[employee_id] = {'name': name,
                                            'age': age,
                                            'position': position,
                                            'salary': salary}

print(valid_employees)
print(invalid_employees)








