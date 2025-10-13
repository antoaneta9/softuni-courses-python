text = input().split(' ')

# second and last letter are switched
# first letter replaced by ascii
result = []
for word in text:
    digits = ''
    for char in word:
        if char.isdigit():
            digits += char
        else:
            break
    first_letter = chr(int(digits))
    rest = word[len(digits):]
    chars = list(first_letter) + list(rest)

    if len(chars) > 2:
        chars[1], chars[-1] = chars[-1], chars[1]

    new_word = ''.join(chars)
    result.append(new_word)
print(' '.join(result))