def absolute_values():
    values = []
    text = input()
    for value in text.split():
        values.append(abs(float(value)))

    return values
result = absolute_values()
print(result)


