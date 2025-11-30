import re

order_id_regex = r'^ORD-\d{5}$'
name_regex = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
address_regex = r'^[A-Z][a-zA-Z]+, .{3,60}$'
single_product_regex = r'^[a-z]+:[1-9][0-9]?$'
total_price_regex = r'^\d+\.\d{2}$'

prices = {
    "apple": 1.00,
    "banana": 0.80,
    "water": 0.50,
    "bread": 1.20,
    "chocolate": 2.50
}

valid_cart = {}
invalid_cart = {}

while True:
    cmd = input()
    if cmd == 'end':
        break

    errors = []
    order_id, name, address, product_list_str, total_price_str = cmd.split(' | ')

    # REGEX validation
    if not re.match(order_id_regex, order_id):
        errors.append("Invalid order ID")
    if not re.match(name_regex, name):
        errors.append("Invalid name")
    if not re.match(address_regex, address):
        errors.append("Invalid address")
    if not re.match(total_price_regex, total_price_str):
        errors.append("Invalid total price format")

    # Process products
    products = {}
    products_sum = 0
    product_list = product_list_str.split(", ")

    for item in product_list:
        if not re.match(single_product_regex, item):
            errors.append(f"Invalid product: {item}")
            continue

        prod, qty = item.split(":")
        qty = int(qty)

        if prod not in prices:
            errors.append(f"Unknown product: {prod}")
            continue

        products[prod] = qty
        products_sum += prices[prod] * qty

    if errors:
        invalid_cart[order_id] = errors
        continue

    total_price = float(total_price_str)

    if round(products_sum, 2) != total_price:
        invalid_cart[order_id] = ["Total price mismatch"]
        continue

    if order_id in valid_cart:
        if total_price < valid_cart[order_id]["total_price"]:
            valid_cart[order_id] = {
                "name": name,
                "address": address,
                "products": products,
                "total_price": total_price
            }
    else:
        valid_cart[order_id] = {
            "name": name,
            "address": address,
            "products": products,
            "total_price": total_price
        }

print("VALID:")
print(valid_cart)
print("INVALID:")
print(invalid_cart)


