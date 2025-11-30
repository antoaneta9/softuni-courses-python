words = input().split()
result=''
for word in words:
    length = len(word)
    result += length * word
print(result)


