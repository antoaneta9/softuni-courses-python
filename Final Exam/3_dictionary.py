dictionary = {}


words_def = input().split(' | ')
for w in words_def:
    word, definition = w.split(': ')
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)

test_words = input().split(' | ')
cmd = input()
if cmd == 'Test':
    for word in test_words:
        if word in dictionary:
            print(f"{word}:")
            for value in dictionary[word]:
                print(f" -{value}")
elif cmd == 'Hand Over':
    for word in dictionary:
        print(word, end=' ')


