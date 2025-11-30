import re

pattern = r'([=/])([A-Z][a-zA-Z]{2,})\1'

text = input()

matches = re.finditer(pattern, text)

destinations = [m.group(2) for m in matches]
travel_points = sum(len(d) for d in destinations)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")