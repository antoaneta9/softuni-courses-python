def characters_in_range(char1, char2):
    start = min(ord(char1), ord(char2))
    end = max(ord(char1), ord(char2))
    result = [chr(code) for code in range(start + 1, end)]
    return ' '.join(result)

char_1 = input()
char_2 = input()
print(characters_in_range(char_1, char_2))
