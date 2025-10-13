string = input().split('.')

integers = list(map(int, string))
for i in range(len(integers) - 1, -1, -1):
    integers[i] += 1
    if integers[i] < 10:
        break
    else:
        integers[i] = 0
        if i == 0:
            integers.insert(0, 1)

print('.'.join(map(str, integers)))

