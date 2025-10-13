text = input().split()
numbers = list(map(int, text))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)



