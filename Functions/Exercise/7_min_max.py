def min_max(numbers):
    numbers_to_list = list(map(int, numbers))
    sum_numbers = sum(numbers_to_list)
    min_value = min(numbers_to_list)
    max_value = max(numbers_to_list)
    return (f'The minimum number is {min_value}\n '
            f'The maximum number is {max_value}\n '
            f'The sum number is: {sum_numbers}')
result = input().split()
print(min_max(result))