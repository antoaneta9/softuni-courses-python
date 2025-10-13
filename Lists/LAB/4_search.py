lines = int(input())
word = input()

all_sentences = []
sentences_with_special_word = []

for i in range(1, lines+1):
    sentence = input()
    all_sentences.append(sentence)
    if word in sentence:
        sentences_with_special_word.append(sentence)

print(all_sentences)
print(sentences_with_special_word)


