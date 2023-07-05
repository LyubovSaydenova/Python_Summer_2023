class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self,attrname):
        if attrname == 'name':
            return object.__getattribute__(self,attrname).title()
        else:
            return object.__getattribute__(self,attrname)

    def __getattr__(self,attrname):
        if attrname == "total":
            return self.price * self.quantity
        else:
            raise AttributeError

