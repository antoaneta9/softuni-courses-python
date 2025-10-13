def tribonacci(a):
    first = 1
    second = 1
    third = 2

    print(first, end=" ")
    if a > 1:
        print(second, end=" ")
    if a > 2:
        print(third, end=" ")

    for i in range(3, a):
        next_number =  first + second + third
        print(next_number, end=' ')
        first, second, third = second, third, next_number

number = int(input())
tribonacci(number)
