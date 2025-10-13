def orders():
    item = input()
    quantity = int(input())
    prices = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }

    total = 0
    if item in prices:
        total += quantity * prices[item]
        return f'{total:.2f}'
    else:
        return "Invalid item"

result = orders()
print(result)