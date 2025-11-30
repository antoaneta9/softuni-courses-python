txt = input()
while True:
    cmd = input()
    if cmd == "Reveal":
        break

    parts = cmd.split(':|:')
    if parts[0] == "InsertSpace":
        index = int(parts[1])
        new_text = f'{txt[:index]} {txt[index:]}'
        txt = new_text
        print(txt)
    elif parts[0] == "Reverse":
        substr = parts[1]
        reverse_substr = substr[::-1]
        if substr in txt:
            new_text = txt.replace(substr, '', 1)
            txt = new_text
            txt += reverse_substr
            print(txt)
        else:
            print('error')
    elif parts[0] == "ChangeAll":
        substr = parts[1]
        replacement = parts[2]
        if substr in txt:
            new_text = txt.replace(substr, replacement)
            txt = new_text
            print(txt)
print(f"You have a new text message: {txt}")