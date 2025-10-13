text = input().split(' ')

text_list = list(filter(lambda x: len(x) % 2==0, text))
print('\n'.join(map(str, text_list)))