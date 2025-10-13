string = input()
count = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, count)
print(result)
