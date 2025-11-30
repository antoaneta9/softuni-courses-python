text = input()
letters = ''
numbers = ''
chars = ''
for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        chars += char
print(f"{numbers} \n{letters} \n{chars}")
