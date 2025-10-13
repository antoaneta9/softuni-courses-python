def factorial(n1, n2):
    result_sum_n1 = 1
    result_sum_n2 = 1
    for i in range(1, n1 + 1):
        result_sum_n1 *= i

    for j in range(1, n2 + 1):
        result_sum_n2 *= j

    devision_sum = result_sum_n1 / result_sum_n2
    return f'{devision_sum:.2f}'

int_1 = int(input())
int_2 = int(input())
print(factorial(int_1, int_2))


