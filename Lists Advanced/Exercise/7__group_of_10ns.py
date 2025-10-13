numbers = list(map(int, input().split(', ')))

boundary = 10

while numbers:
    current_group = [num for num in numbers if num <= boundary]
    numbers = [num for num in numbers if num > boundary]
    print(f"Group of {boundary}'s: {current_group}")
    boundary += 10
