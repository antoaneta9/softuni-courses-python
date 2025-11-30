dictionary = {}
while True:
    text = input()
    if text == 'Lumpawaroo':
        break

    if ' | ' in text:
        force_side, force_user = text.split(' | ')
        user_exist = any(force_user in users for users in dictionary.values())
        if not user_exist:
            if force_side not in dictionary:
                dictionary[force_side] = []
            dictionary[force_side].append(force_user)
        else:
            continue

    elif ' -> ' in text:
        force_user, force_side = text.split(' -> ')
        for side, users in dictionary.items():
            if force_user in users:
                users.remove(force_user)
                break
        if force_side not in dictionary:
            dictionary[force_side] = []
        dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for key, value in dictionary.items():
    if value:
        print(f"Side: {key}, Members: {len(value)}")
        print('!', '\n! '.join(value))

