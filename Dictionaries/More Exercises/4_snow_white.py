from collections import Counter
dwarfs = {}
input_order = []
while True:
    command = input()
    if command == 'Once upon a time':
        break
    name, hat_color, physics_ = command.split(' <:> ')
    physics = int(physics_)

    if name not in dwarfs:
        dwarfs[name] = {}

    if hat_color not in dwarfs[name]:
        dwarfs[name][hat_color] = physics

    if dwarfs[name][hat_color] < physics:
        dwarfs[name][hat_color] = physics

# BY PHYSICS -> DESC ORDER
# BY TOTAL COUNT OF DWARFS W SAME HAT ->DESC ORDER
all_dwarfs = []
for name, hats in dwarfs.items():
    for color, physics in hats.items():
        all_dwarfs.append((name, color, physics))
print(all_dwarfs)
print('<------------------------------------------------->')
hat_counts = Counter([color for _, color, _ in all_dwarfs])
print(hat_counts)
print('<------------------------------------------------->')
all_dwarfs.sort(key=lambda x: (-x[2], -hat_counts[x[1]]))
for name, color, physics in all_dwarfs:
    print(f"({color}) {name} <-> {physics}")



