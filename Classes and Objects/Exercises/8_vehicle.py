class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        result = ''
        if self.price <= money and self.owner is None:
            change = money - self.price
            result+= f"Successfully bought a {self.type}. Change: {change:.2f}"
            self.owner = owner
        elif self.owner is not None:
            result += 'Car already sold'
        elif self.price > money:
            result += 'Sorry, not enough money'
        return result

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return 'Vehicle has no owner'
        return self.owner

    def __repr__(self):
        result = ''
        if self.owner is not None:
            result += f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result += f"{self.model} {self.type} is on sale: {self.price}"
        return result


vehicle_type = 'car'
model = "BMW"
price = 30000
vehicle = (Vehicle(vehicle_type, model, price))
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)