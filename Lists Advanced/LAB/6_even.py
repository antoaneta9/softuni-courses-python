text = list(map(int, input().split(', ')))

indexes = [i for i in range(len(text)) if text[i] % 2 == 0]
print(indexes)
