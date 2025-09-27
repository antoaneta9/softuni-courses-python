numbers_count = int(input())

for i in range(numbers_count):
    given_number = int(input())
    if given_number % 2 == 1:
        print(f'{given_number} is odd!')
        break
else:
    print('All numbers are even.')
