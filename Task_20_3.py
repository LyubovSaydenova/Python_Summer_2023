import itertools
class CycleAlfaNumbers:
    def __init__(self):
        self.alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = 0
        self.alfa_number = True
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 26 and self.alfa_number:
            self.index = 0
        if self.alfa_number:
            self.index += 1
            self.alfa_number = not self.alfa_number
            return self.index
        else:
            self.alfa_number = not self.alfa_number
            return self.alfa[self.index - 1]
f = CycleAlfaNumbers()
for _ in range(60):
    print(next(f), end = ',')