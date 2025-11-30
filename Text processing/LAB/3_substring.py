word_to_remove = input()
sentence = input()

while word_to_remove in sentence:
    sentence = sentence.replace(word_to_remove, "")
print(sentence)