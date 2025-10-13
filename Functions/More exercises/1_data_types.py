def data_types(type, data):
    result = ''

    if type == 'int':
        result = int(data) * 2
    elif type == 'real':
        formatted_result = float(data) * 1.5
        result = f"{formatted_result:.2f}"
    elif type == 'string':
        result = '$'+str(data)+'$'

    return result

data_type = input()
char = input()
call = data_types(data_type, char)
print(call)
