notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break

    parts = command.split('-')
    importance = int(parts[0]) - 1
    note = parts[1]

    notes.pop(importance)
    notes.insert(importance, note)

result = [el for el in notes if el != 0]
print(result)