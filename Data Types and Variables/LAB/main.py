from enum import unique

year = int(input()) + 1
while True:
    year_str = str(year)
    unique_digits = set(year_str)
    if len(unique_digits) == len(year_str):
        print(year)
        break
    year += 1






