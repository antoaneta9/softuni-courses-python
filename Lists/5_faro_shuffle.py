string = input().split()
shuffle_count=int(input())

half_str = len(string) // 2

index_zero = string[0]
last_index = string[-1]

shuffled = []
for i in range(half_str):
    shuffled.append(string[i])
print(index_zero,shuffled, last_index)

