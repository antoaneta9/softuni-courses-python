employees_happiness = input().split(' ')
factor = int(input())

multipl_empl_happiness = list(map(lambda x: int(x) * factor, employees_happiness))
average = list(filter(lambda x: x >= (sum(multipl_empl_happiness) / len(employees_happiness)), multipl_empl_happiness))

if len(average) >= len(employees_happiness) /2:
    print(f"Score: {len(average)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(average)}/{len(employees_happiness)}. Employees aren't happy!")

