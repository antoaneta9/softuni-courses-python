def perfect_number(number):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
            if sum_of_divisors == number:
                return 'We have a perfect number!'

    return "It's not so perfect."
answer = int(input())
print(perfect_number(answer))

