
phonebook = {}
while True:
    text = input()
    if text == "search":
        break

    name, phone = text.split('-')
    if name not in phonebook:
        phonebook[name] = phone

while True:
    command = input()
    if command == 'stop':
        break
    name = command
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist")


