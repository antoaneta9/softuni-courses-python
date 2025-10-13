string = input().split()
shuffle_count = int(input())


for _ in range(shuffle_count):
    half = len(string) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(string[i])
        shuffled.append(string[half + i])
    string = shuffled.copy()

print(string)


