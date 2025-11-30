class Inventory:
    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item):
        result = ''
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            result += 'not enough room in the inventory'
        return result

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return (f"Items: {', '.join(self.items)}.\n"
                f"Capacity left: {self.__capacity - len(self.items)}")

inventory = Inventory(2)

inventory.add_item("potion")

inventory.add_item("sword")

print(inventory.add_item("bottle"))

print(inventory.get_capacity())

print(inventory)

