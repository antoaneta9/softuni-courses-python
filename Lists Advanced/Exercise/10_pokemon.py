text = input().split()
integers = list(map(int, text))

popped_pokemons = []

while len(integers) > 0:
    indexes = int(input())

    if indexes < 0:
        removed = integers[0]
        integers[0] = integers[-1]
    elif indexes >= len(integers):
        removed = integers[-1]
        integers[-1] = integers[0]
    else:
        removed = integers.pop(indexes)

    popped_pokemons.append(removed)

    for i in range(len(integers)):
        if integers[i] <= removed:
            integers[i] += removed
        else:
            integers[i] -= removed
print(sum(popped_pokemons))



