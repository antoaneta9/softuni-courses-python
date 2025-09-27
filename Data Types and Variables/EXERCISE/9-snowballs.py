
lines = int(input())
best_value = 0
best_weight = 0
best_time = 0
best_quality = 0

for line in range(1, lines +1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (weight / time) ** quality
    if snowball_value > best_value:
        best_value = snowball_value
        best_weight = weight
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")
