text = input()
result = []
for i in range(len(text)):
    if text[i] == ":":
        result.append(text[i] + text[i+1])
print('\n'.join(result))