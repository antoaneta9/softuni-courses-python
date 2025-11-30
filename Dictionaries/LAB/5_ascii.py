characters = input().split(', ')

dict_ascii = {value: ord(value) for value in characters}
print(dict_ascii)
