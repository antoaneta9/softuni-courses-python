def is_palindrome(numbers):
    numbers_to_list = list(map(int, numbers))
    answer = []

    for n in numbers_to_list:
        if str(n) == str(n)[::-1]:
            answer.append(True)
        else:
            answer.append(False)
    return answer


input_numbers = input().split(', ')
result = is_palindrome(input_numbers)

for r in result:
    print(r)