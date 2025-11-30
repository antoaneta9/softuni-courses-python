def factorial(n):
    if n == 0:
        return 1          # база
    else:
        return n * factorial(n - 1)  # рекурсивно извикване

print(factorial(5))  # Изход: 120
