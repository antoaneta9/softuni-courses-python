def calculator(num_1, num_2, operator):
    result = None

    if operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    elif operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        if num_1 != 0 and num_2 != 0:
            result = int(num_1 / num_2)
        else:
            result = 'Division by zero'

    return result

try_1 = calculator()
print(try_1)
