elements = input().split(' ')
el_dict = {}

for element in elements:
    word = element.lower()
    if word not in el_dict:
        el_dict[word] = 0
    el_dict[word] +=1

for (key, value) in el_dict.items():
    if value % 2 == 1:
        print(key, end=' ')