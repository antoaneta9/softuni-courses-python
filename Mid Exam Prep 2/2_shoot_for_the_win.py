targets = list(map(int, input().split()))
count = 0

while True:
    command = input()
    if command == 'End':
        break

    index_command = int(command)
    if 0 <= index_command < len(targets):
        shot_value = targets[index_command]
        if targets[index_command] == -1:
            continue

        count+=1
        targets[index_command] = -1

        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > shot_value:
                    targets[i] -= shot_value
                else:
                    targets[i] += shot_value



print(f"Shot targets: {count} -> {' '.join(map(str, targets))}")