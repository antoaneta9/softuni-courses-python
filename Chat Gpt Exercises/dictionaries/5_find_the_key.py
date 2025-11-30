contacts = {}
while True:
    command = input()
    if command == 'stop':
        break

    name, number = command.split()
    if name not in contacts:
        contacts[name] = number

find_name = input()
if find_name in contacts:
    print(f"{find_name} -> {contacts[find_name]}")
else:
    print("Not found")