import re
names = input()
patter = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
result = re.findall(patter, names)
print(' '.join(result))