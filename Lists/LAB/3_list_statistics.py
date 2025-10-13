lines = int(input())
negatives_sum = 0
positive_count = 0

negative_numbers = []
positive_numbers = []

for i in range(1, lines + 1):
    number = int(input())
    if number < 0:
        negative_numbers.append(number)
        negatives_sum += number
    elif number >= 0:
        positive_count += 1
        positive_numbers.append(number)


print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negatives_sum}')

