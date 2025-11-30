word = input().lower()
letters = {letter: word.count(letter) for letter in word}
print(letters)