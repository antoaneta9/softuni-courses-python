items = input().split('|')
budget = float(input())

bought_items = []
for item in items:
    type_, price_ = item.split('->')
    price = float(price_)

    if price > budget:
        continue

    if type_ == 'Clothes' and price >= 50:
        continue
    elif type_ == 'Shoes' and price >= 35:
        continue
    elif type_ == 'Accessories' and price >= 20.50:
        continue
    else:
        bought_items.append(price)
        budget -= price
#
# print(items)
# print(budget)
new_prices = []
for item in bought_items:
    item *= 1.40
    new_prices.append(round(item,2))
print(*new_prices)
total_sold_items = sum(new_prices)
total = budget + total_sold_items
profit = total_sold_items - sum(bought_items)
print(f"Profit: {profit:.2f}")
if total >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')



