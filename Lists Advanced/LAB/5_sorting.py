input_names = input().split(', ')

length_sorting = sorted(input_names, key = lambda x: (-len(x), x))
print(length_sorting)