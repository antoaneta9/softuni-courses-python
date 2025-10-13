
string = input().split(', ')
substring = input().split(', ')

new_text = [word for word in string if any(word in s for s in substring)]
print(new_text)