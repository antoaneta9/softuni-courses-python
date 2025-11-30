dictionary = {}

while True:
    text = input()
    if text == 'stop':
        break

    name, grade_str = text.split()
    grade = float(grade_str)
    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(grade)

for (key, value) in dictionary.items():
    avg = sum(value) / len(value)
    print(f"{key} -> {avg:.2f}")




