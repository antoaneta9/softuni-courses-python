import re

text = input()

pattern = r'([#|])([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(10000|[0-9]{1,4})\1'

matches = re.findall(pattern, text)

total_calories = sum(int(m[3]) for m in matches)
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for m in matches:
    print(f"Item: {m[1]}, Best before: {m[2]}, Nutrition: {m[3]}")
