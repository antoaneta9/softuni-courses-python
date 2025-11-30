import re

artifact_regex = r'[*^]+([A-Za-z ]{6,})[*^]+[^A-Za-z0-9]*\++([0-9.-]+,[0-9.-]+)\++'

text = input()

matches = list(re.finditer(artifact_regex, text))

if not matches:
    print('No valid artifacts found.')
else:
    for match in matches:
        artifact = match.group(1).strip()
        coordinates = match.group(2)
        print(f"Found {artifact} at coordinates {coordinates}.")

