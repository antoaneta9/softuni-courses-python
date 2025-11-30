import re

dates = input()
pattern = r'\b[0-9][0-9]\/[A-Z][a-z][a-z]\/[0-9][0-9][0-9][0-9]|[0-9][0-9]\-[A-Z][a-z][a-z]\-[0-9][0-9][0-9][0-9]|[0-9][0-9]\.[A-Z][a-z][a-z]\.[0-9][0-9][0-9][0-9]\b'
result = re.findall(pattern, dates)
# print(result)

for item in result:
    day = item[0] + item[1]
    month = item[3] + item[4] + item[5]
    year = item[7] + item[8] + item[9] + item[10]
    print(f"Day: {day}, Month: {month}, Year: {year}")


