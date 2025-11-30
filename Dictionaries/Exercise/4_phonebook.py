contacts = {}
lines_to_check = 0
while True:
    text = input()
    if text.isnumeric():
        lines_to_check = int(text)
        break

    name, tel_number = text.split('-')
    if name not in contacts:
        contacts[name] = tel_number
    elif name in contacts:
        contacts[name] = tel_number

for num in range(lines_to_check):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
