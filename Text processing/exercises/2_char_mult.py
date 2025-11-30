str1, str2 = input().split()
print(str1, str2)
min_len = min(len(str1), len(str2))
total = 0
for i in range(min_len):
    total += ord(str1[i]) * ord(str2[i])
if len(str1) > len(str2):
    for ch in str1[min_len:]:
        total += ord(ch)
elif len(str2) > len(str1):
    for ch in str2[min_len:]:
        total += ord(ch)
print(total)


