text = list(map(int, input().split()))
sum_of_nums = sum(text)
average = sum_of_nums / len(text)
desc_sort = sorted(text, reverse=True)
result = []
for number in desc_sort:

    if number > average:
        result.append(number)
        if len(result) == 5:
            break

if result == []:
    print('No')
print(*result)
