class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product, price: float, quantity=1):
        if product not in self.products:
            self.products[product] = {"price": price, "quantity": quantity}
        else:
            self.products[product]["quantity"] += quantity

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]

    def update_price(self, product, price):
        if product in self.products:
            self.products[product]["price"] = price

    def get_total_value(self):
        total = 0
        for product in self.products.values():
            total += product["price"] * product["quantity"]
        return round(total, 2)

    def most_expensive(self):
        if not self.products:
            return 'No products available'
        max_product = max(self.products, key=lambda name: self.products[name]["price"])
        price = self.products[max_product]["price"]
        return f"Most expensive: {max_product} ({price:.2f} lv)"

    def __str__(self):
        print(f"Store: {self.name}\n")
        result = ''
        for product, price in self.products.items():
            result += f"{product} -> {price['price']:.2f} lv (price: {price['quantity']} pcs)\n)"
        return result

store = Store("SuperMart")

store.add_product("Bread", 1.20, 50)
store.add_product("Milk", 2.30, 20)
store.add_product("Eggs", 0.30, 200)

store.update_price("Eggs", 0.35)

print(store)
print("Total store value:", store.get_total_value())
print(store.most_expensive())

