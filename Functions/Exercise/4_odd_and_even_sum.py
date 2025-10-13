def sum_of_all(number):
    split_number = list(map(int, number))

    sum_of_even = 0
    sum_of_odd = 0

    for number in split_number:
        if number % 2 == 0:
            sum_of_even += number
        if number % 2 == 1:
            sum_of_odd += number
    return f'Odd sum: {sum_of_odd}, Even sum: {sum_of_even}'

numbers = input()
print(sum_of_all(numbers))

