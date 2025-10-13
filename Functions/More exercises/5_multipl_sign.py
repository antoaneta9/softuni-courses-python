def multiplication_sign(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"

    negative_count = 0
    for num in [n1, n2, n3]:
        if num < 0:
            negative_count += 1

    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(multiplication_sign(num_1, num_2, num_3))