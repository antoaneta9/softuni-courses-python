storage = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in storage:
        storage[resource] = 0
    storage[resource] += quantity

for key, value in storage.items():
    print(f"{key} -> {value}")


