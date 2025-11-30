
reversed_words = {}
while True:
    word = input()
    if word == "end":
        break
    reversed_word = word[::-1]
    if word not in reversed_words:
        reversed_words[word] = ''
    reversed_words[word] = reversed_word

for word, reversed_word in reversed_words.items():
    print(f"{word} = {reversed_word}")


