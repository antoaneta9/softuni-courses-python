import re
barcode_r = r'^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$'
matches = []
lines = int(input())

for _ in range(lines):
    line = input()
    if re.match(barcode_r, line):
        digits = ''.join(ch for ch in line if ch.isdigit())
        if digits:
            print(f"Product group: {digits}")
        else:
            print(f"Product group: 00")
    else:
        print('Invalid barcode')

