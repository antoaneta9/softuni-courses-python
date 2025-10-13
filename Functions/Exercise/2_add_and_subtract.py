def add_and_subtract(a, b, c):

    def add():
        return a + b

    def subtract():
        return add() - c

    return subtract()

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = add_and_subtract(num_1, num_2, num_3)
print(result)