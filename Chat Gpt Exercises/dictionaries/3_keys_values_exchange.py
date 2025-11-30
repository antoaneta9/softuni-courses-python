dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
}

new_dict = {}
for key, value in dictionary.items():
    new_dict[value] = key
print(new_dict)
