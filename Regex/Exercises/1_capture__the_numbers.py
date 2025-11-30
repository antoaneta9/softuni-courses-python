import re

pattern = r'\d+'
text = input()
matches = []
while text:
    match = re.findall(pattern, text)
    if match:
        matches+=match

    text = input()
print(' '.join(matches))



