line = int(input())
dictionary = {}

for i in range(line):
    words = input()
    synonyms = input()
    if words not in dictionary:
        dictionary[words] = []
    dictionary[words].append(synonyms)


for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
