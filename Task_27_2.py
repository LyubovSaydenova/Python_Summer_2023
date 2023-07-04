class Item:
    """Item description"""
    emp = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.emp += 1

    def display_item(self):
        print('Item')

    def display_total(self):
        print(self.price * self.quantity)