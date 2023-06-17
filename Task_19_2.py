class Fibo:
    def __init__(self):
        self.a = -1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
f = Fibo()
for _ in range(10):
    print(next(f))