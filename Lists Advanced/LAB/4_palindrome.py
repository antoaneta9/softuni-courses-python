words = input().split(' ')
palindrome_word = input()

palindromes = []
for word in words:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome_word)} times")