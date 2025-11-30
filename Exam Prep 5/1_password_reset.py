
result = input()
while True:
    cmd = input()
    if cmd == 'Done':
        break

    parts = cmd.split()
    if parts[0] == 'TakeOdd':
        password = "".join(result[i] for i in range(len(result)) if i % 2 == 1)
        result = password
        print(result)
    elif parts[0] == 'Cut':
        index = int(parts[1])
        length = int(parts[2])
        substring = result[index:index+length]
        passowrd = result.replace(substring, '', 1)
        result = passowrd
        print(result)
    elif parts[0] == 'Substitute':
        substring = parts[1]
        substitute = parts[2]
        if substring in result:
            new_res = result.replace(substring, substitute)
            result = new_res
            print(result)
        else:
            print('Nothing to replace!')
print(f"Your password is: {result}")