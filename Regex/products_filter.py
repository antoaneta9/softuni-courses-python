import re

product_name_regex = r'^[A-Z][A-Za-z0-9 ]{2,}$'
price_regex = r'^\d+(\.\d{1,2})?$'
categories_regex = r'^[a-zA-Z]{3,}$'
sku_regex = r'^[A-Z]{3}-\d{5}$'

valid_products = {}
invalid_products = {}

while True:
    cmd = input()
    if cmd == 'end':
        break
    product_name, price, category, sku = cmd.split(' | ')
    errors = []

    if not re.match(product_name_regex, product_name):
        errors.append('Invalid product name')
    if not re.match(price_regex, price):
        errors.append('Invalid price')
    if not re.match(categories_regex, category):
        errors.append('Invalid category')
    if not re.match(sku_regex, sku):
        errors.append('Invalid SKU')

    if not errors:
        price = float(price)
        if product_name in valid_products:
            if price > valid_products[product_name]['price']:
                valid_products[product_name]['price'] = price
        else:
            valid_products[product_name] = {
                'price': price,
                'category': category,
                'sku': sku
            }
    else:
        invalid_products[product_name] = errors
print('INVALID PRODUCTS:')
print(invalid_products)
print('VALID PRODUCTS:')
print(valid_products)