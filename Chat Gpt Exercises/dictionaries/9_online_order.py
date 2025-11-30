
dictionary = {}
while True:
    command = input()
    if command == "stop":
        break
    name, food, quantity_str, price_str = command.split()
    if name not in dictionary:
        dictionary[name] = []
        