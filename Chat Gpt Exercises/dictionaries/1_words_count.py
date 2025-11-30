sentence = input().split()
dictionary = {word: sentence.count(word) for word in sentence}
print(dictionary)