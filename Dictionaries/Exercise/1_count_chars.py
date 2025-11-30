text = input()
dictionary = {ch: text.count(ch) for ch in text if ch != ' '}
for char in dictionary:
    print(f"{char} -> {dictionary[char]}")