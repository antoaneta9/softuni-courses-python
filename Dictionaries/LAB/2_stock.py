items = input().split()
stock = {}
for i in range(0, len(items), 2):
    key = items[i]
    value = int(items[i + 1])
    stock[key] = value

stuff = input().split()
for item in stuff:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
