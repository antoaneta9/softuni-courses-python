text = input()
result = ""
for char in text:
    if 32 <= ord(char) <= 126:
        result += chr((ord(char) - 32 + 3) % 95 + 32)
    else:
        result += char

print(result)