import re
text = input()
patter = r'(\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4})\b'
result = re.findall(patter, text)
print(' '.join(result))