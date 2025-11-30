def string_explode(text):
    result = []
    strength = 0
    for i in range(len(text)):
        if text[i] == '>':
            result.append('>')
            strength += int(text[i+1])
        else:
            if strength > 0:
                strength -= 1
            else:
                result.append(text[i])
    return ''.join(result)

res = input()
print(string_explode(res))