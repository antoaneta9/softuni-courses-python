
word = input()
backwards_word = ''
for letter in range(len(word) -1, -1, -1):
    backwards_word += word[letter]
print(backwards_word)