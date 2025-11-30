text =input()

while True:
    cmd = input()
    if cmd == "Travel":
        break
    parts = cmd.split(':')

    if parts[0] == "Add Stop":
        index = int(parts[1])
        string = parts[2]
        if 0 <= index <= len(text):
            new_text = text[:index] + string + text[index:]
            text = new_text
        print(text)
    elif parts[0] == "Remove Stop":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if 0 <= start_index <= end_index < len(text):
            new_text = text[:start_index] + text[end_index + 1:]
            text = new_text
        print(text)
    elif parts[0] == "Switch":
        old_string = parts[1]
        new_string = parts[2]
        if old_string in text:
            new_text = text.replace(old_string, new_string)
            text = new_text
        print(text)
print(f'Ready for world tour! Planned stops: {text}')


