chars = int(input())
total_sum = 0
for i in range(chars):
    char = input()
    total_sum += ord(char)
print(f'Total sum equals: {total_sum}')