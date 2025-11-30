text = input()
while True:
    cmd = input()
    if cmd == 'Decode':
        break
    action, info = cmd.split(' ', maxsplit=1)
    if action == 'Move':
        symbols = int(info)
        if len(text) > symbols:
            new_t = text[:symbols]
            new_text = text[symbols:] + new_t
            text = new_text
            print(text)
        else:
            print('Word too short')
    elif action == 'Insert':
        index_, value = info.split()
        index = int(index_)
        if 0 <= index <= len(text):
            new_text = text[:index] + value + text[index:]
            text = new_text
            print(text)
        else:
            print('Word too long/No such index')
    elif action == 'ChangeAll':
        substring, replacement = info.split()
        new_t = text.replace(substring, replacement)
        text = new_t
        print(text)
print(f"The decrypted message is: {text}")

