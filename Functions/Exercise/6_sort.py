def sorting(numbers):
    numbers_to_list= list(map(int, numbers))
    ascending = list(sorted(numbers_to_list))
    return ascending
text = input().split()
print(sorting(text))

