contacts = {}
while True:
    command = input()
    if command == "stop":
        break
    name, telephone = command.split()
    if name not in contacts:
        contacts[name] = telephone

while True:
    command = input()
    if command == "stop":
        break

    name, new_telephone = command.split()
    if name in contacts:
        contacts[name] = new_telephone
    elif name not in contacts:
        contacts[name] = new_telephone
print(contacts)





