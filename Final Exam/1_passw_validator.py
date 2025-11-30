password = input()
while True:
    cmd = input()
    if cmd == 'Complete':
        break
    parts = cmd.split(' ')
    if parts[0] == 'Make':
        command, index = parts[1], int(parts[2])
        if 0 <= index < len(password):
            if command == "Upper":
                new_p = password[:index] + password[index].upper() + password[index + 1:]
                password = new_p
            elif command == "Lower":
                new_p = password[:index] + password[index].lower() + password[index + 1:]
                password = new_p
            print(password)
        else:
            continue

    elif parts[0] == 'Insert':
        index, char = int(parts[1]), parts[2]
        if 0<= index <= len(password):
            new_p = password[:index] + char + password[index:]
            password = new_p
            print(password)
        else:
            continue

    elif parts[0] == 'Replace':
        char, value = parts[1], int(parts[2])
        if char in password:
            ascii_value = chr(ord(char) + value)
            new_p = password.replace(char, ascii_value)
            password = new_p
            print(password)
        else:
            continue

    elif parts[0] =='Validation':
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        if not all(ch.isalnum() or ch == "_" for ch in password):
            print("Password must consist only of letters, digits and _!")

        if not any(ch.isupper() for ch in password):
            print("Password must consist at least one uppercase letter!")

        if not any(ch.islower() for ch in password):
            print("Password must consist at least one lowercase letter!")

        if not any(ch.isdigit() for ch in password):
            print("Password must consist at least one digit!")



