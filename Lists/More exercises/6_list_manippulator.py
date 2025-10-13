data = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'exchange':
        index = int(command[1])
        if 0 <= index < len(data):
            data = data[index + 1:] + data[:index + 1]
        else:
            print("Invalid index")
    elif command[0] == 'max':
        if command[1] == 'even':
            evens = [n for n in data if n % 2 == 0]
            if evens:
                max_even = max(evens)
                print(len(data) - 1 - data[::-1].index(max_even))
            else:
                print('No matches')
        elif command[1] == 'odd':
            odds = [n for n in data if n % 2 == 1]
            if odds:
                max_odd = max(odds)
                print(len(data) - 1 - data[::-1].index(max_odd))
            else:
                print('No matches')
    elif command[0] == 'min':
        if command[1] == 'even':
            evens = [n for n in data if n % 2 == 0]
            if evens:
                min_even = min(evens)
                print(len(data) - 1 - data[::-1].index(min_even))
            else:
                print('No matches')
        elif command[1] == 'odd':
            odds = [n for n in data if n % 2 == 1]
            if odds:
                min_odd = min(odds)
                print(len(data) - 1 - data[::-1].index(min_odd))
            else:
                print('No matches')

    elif command[0] == 'first':
        count = int(command[1])
        even_or_odd = command[2]

        if count > len(data):
            print("Invalid count")
        else:
            if even_or_odd == 'even':
                filtered = [x for x in data if x % 2 == 0]
            else:
                filtered = [x for x in data if x % 2 == 1]
            print(filtered[:count])
    elif command[0] == 'last':
        count = int(command[1])
        even_or_odd = command[2]

        if count > len(data):
            print("Invalid count")
        else:
            if even_or_odd == 'even':
                filtered = [x for x in data if x % 2 == 0]
            else:
                filtered = [x for x in data if x % 2 == 1]
            print(filtered[-count:])
print(data)



