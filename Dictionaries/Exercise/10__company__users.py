data = {}

while True:
    text = input()
    if text == 'End':
        break
    company, employee_id = text.split(' -> ')
    if company not in data:
        data[company] = []
    if employee_id not in data[company]:
        data[company].append(employee_id)

for key, value in data.items():
    print(key)
    for v in value:
        print(f"-- {v}")