import re
text = input()
sites = []
pattern = r'www\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}'

while text:
    matches = re.findall(pattern, text)
    for match in matches:
        sites.append(match)
    text = input()
print('\n'.join(sites))

