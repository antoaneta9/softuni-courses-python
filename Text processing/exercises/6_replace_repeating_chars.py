def remove_repeating_chars(text):
    result = text[0]
    for char in text[1:]:
        if char != result[-1]:
            result += char
    return result
some_txt = input()
res = remove_repeating_chars(some_txt)
print(res)
