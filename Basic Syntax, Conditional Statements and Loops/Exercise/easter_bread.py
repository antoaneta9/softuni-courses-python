budget = float(input())
flour_price_per_kg = float(input())
eggs_price_packet = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg * 1.25

milk_price_for_250ml= milk_price_per_liter * 0.25

loaf_cost = (flour_price_per_kg + eggs_price_packet + milk_price_for_250ml)
loaves_count = 0
colored_eggs = 0

while budget > loaf_cost:
    loaves_count += 1
    colored_eggs+=3
    budget -= loaf_cost
    if loaves_count % 3 == 0:
        colored_eggs -= (loaves_count - 2)


print(f'You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} colored eggs and {budget:.2f}BGN left.')



