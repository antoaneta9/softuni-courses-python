data = input().split()

while True:
    command = input().split()
    if command[0] == '3:1':
        break

    if command[0] == 'merge':
        start = max(0, int(command[1]))
        end = min(len(data) - 1, int(command[2]))

        if start > end:
            continue

        merged = ''.join(data[start:end + 1])
        data[start:end + 1] = [merged]

    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])

        if partitions <= 0:
            continue

        element = data[index]
        part_size = len(element) // partitions
        remainder = len(element) % partitions

        new_parts = []
        start_idx = 0

        for i in range(partitions - 1):
            end_idx = start_idx + part_size
            new_parts.append(element[start_idx:end_idx])
            start_idx = end_idx

        new_parts.append(element[start_idx:])

        data[index:index + 1] = new_parts

print(' '.join(data))

