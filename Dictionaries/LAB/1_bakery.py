text = input().split()
bakery = {}
for i in range(0, len(text), 2):
    key = text[i]
    value = int(text[i + 1])
    bakery[key] = value
print(bakery)

