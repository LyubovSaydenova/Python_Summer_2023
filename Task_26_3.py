class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self): return self._age
    @age.setter
    def age(self, age):
        if age < 1 or age > 100: print('Недопустимый возраст')
        else: self._age = age
    @age.deleter
    def age(self): del self._age
p = Person(25)
print(p.age)
p.age = 0
p.age = 101
p.age = 55
print(p.age)
del p.age
print(p.__dict__)