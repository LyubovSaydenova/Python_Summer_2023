class Breakfast:
    def __init__(self, *pay):
        self.pay = list(pay)
    def __getitem__(self, i):
        return self.pay[i]
class Customer:
    def __init__(self):
        self.buy = 0
    def drink(self, pay, *cup):
        for i in cup:
            i.cost(pay)
            self.buy += 1
class Cup:
    def __init__(self):
        self.payment = []
    def cost(self, pay):
        self.payment.append(pay)
cafe = Breakfast('by card', 'in cash')
visitor = Customer()
cup_of_coffee = Cup()
cup_of_tea = Cup()
visitor.drink(cafe[0], cup_of_coffee)
visitor.drink(cafe[1], cup_of_tea)
print(f"cup_of_coffee {cup_of_coffee.payment}")
print(f"cup_of_tea {cup_of_tea.payment}")