word = list(input())
vowels = ['a', 'e', 'i', 'o', 'u']

no_vowels = [letter for letter in word if letter.lower() not in vowels]
print(''.join(no_vowels))