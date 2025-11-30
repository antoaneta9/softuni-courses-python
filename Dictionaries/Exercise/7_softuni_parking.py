registered_people = {}
lines = int(input())

for line in range(lines):
    text = input().split()
    if len(text) == 3:
        validation, username, license_ = text
        if validation == 'register':
            if username not in registered_people:
                registered_people[username] = license_
                print(f"{username} registered {license_} successfully")
            else:
                print(f"ERROR: already registered with plate number {registered_people[username]}")
    elif len(text) == 2:
        validation, username = text
        if validation == 'unregister':
            if username in registered_people:
                print(f"{username} unregistered successfully")
                del registered_people[username]
            else:
                print(f"ERROR: user {username} not found")

for key, value in registered_people.items():
    print(f"{key} => {value}")


