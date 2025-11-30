import re

text = input()
digits_r = r'\d+'
emoji_regex = r"(::|\*\*)([A-Z][a-z]{2,})\1"

matches = re.findall(emoji_regex, text)

words= []
for match in matches:
    word = match[1]
    words.append(word)

digits_collection = []
for char in text:
    if re.match(digits_r, char):
        digits_collection.append(int(char))
    else:
        continue
sum_d = 1
for i in digits_collection:
    sum_d = int(sum_d * i)

print(f"Cool threshold: {sum_d}")
print(f"{len(words)} emojis found in the text. The cool ones are:")
for delimeter, word in matches:
    full_emoji = f"{delimeter}{word}{delimeter}"
    coolness = sum(ord(ch) for ch in word)
    if coolness >= sum_d:
        print(full_emoji)



