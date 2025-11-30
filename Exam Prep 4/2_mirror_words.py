import re
word_r = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
text = input()
matches = list(re.finditer(word_r, text))
if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

mirror_words = []

for match in matches:
    symbol, word1, word2 = match.groups()
    if word1 == word2[::-1]:
        mirror_words.append(f"{word1} <=> {word2}")

if mirror_words:
    print("The mirror words are:")
    print(", ".join(f"{mw}" for mw in mirror_words))
else:
    print("No mirror words!")


