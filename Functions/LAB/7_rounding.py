def rounding():
    number = input().split()
    rounded_number = []
    for n in number:
        rounded_number.append(round(float(n)))
    return rounded_number
result = rounding()
print(result)