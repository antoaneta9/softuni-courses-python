numbers = list(map(int, input().split()))
middle = len(numbers) // 2

left_side = list(numbers[:middle])
right_side = list(reversed(numbers[middle + 1:]))

total_right = 0
total_left = 0

for num in right_side:
    if num == 0:
        total_right *= 0.8
    else:
        total_right += num

for num in left_side:
    if num == 0:
        total_left *= 0.8
    else:
        total_left += num


# print(total_right)
# print(total_left)

if total_left > total_right:
    print(f"The winner is right with total time: {total_right:.1f}")
elif total_right > total_left:
    print(f"The winner is left with total time: {total_left:.1f}")
else:
    print(f"Game is even.")