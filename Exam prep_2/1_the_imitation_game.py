decrypted_mess = input()

while True:
    cmd = input()
    if cmd == 'Decode':
        break
    parts = cmd.split('|')

    if parts[0] == 'Move':
        letters_num = int(parts[1])
        word = decrypted_mess[letters_num:] + decrypted_mess[:letters_num]
        decrypted_mess = word
    elif parts[0] == 'Insert':
        index = int(parts[1])
        value = parts[2]
        if 0 <= index <= len(decrypted_mess):
            word = decrypted_mess[:index] + value + decrypted_mess[index:]
            decrypted_mess = word
    elif parts[0] == 'ChangeAll':
        substring = parts[1]
        replacement = parts[2]
        word = decrypted_mess.replace(substring, replacement)
        decrypted_mess = word

print(f"The decrypted message is: {decrypted_mess}")

