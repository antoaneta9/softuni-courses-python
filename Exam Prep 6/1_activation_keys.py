text = input()
while True:
    cmd = input()
    if cmd == 'Generate':
        break

    parts = cmd.split('>>>')
    if parts[0] == 'Contains':
        substring = parts[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print('Substring not found!')
    elif parts[0] == 'Flip':
        type_ = parts[1]
        start_index = int(parts[2])
        end_index = int(parts[3])
        if type_ == 'Upper':
            new_text = text.replace(text[start_index:end_index], text[start_index:end_index +1].upper())
            text = new_text
        if type_ == 'Lower':
            new_text = text.replace(text[start_index:end_index], text[start_index:end_index +1].lower())
            text = new_text
        print(text)
    elif parts[0] == 'Slice':
        start_index = int(parts[1])
        end_index = int(parts[2])
        new_text = text.replace(text[start_index:end_index], "")
        text = new_text
        print(text)
print(f"Your activation key is: {text}")