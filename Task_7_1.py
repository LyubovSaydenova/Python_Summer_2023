def noc(list):
    def nod(a, b):
        while a != b and a > 0:
            a, b = max(a,b), min(a,b)
            a = a % b
        return b
    def noc(a, b):
        return a * b // nod(a, b)
    y = 1
    for i in list:
        y = noc(y, i)
    return y
print(noc(list(map(int, input('-->').split()))))
и ещё решение
from math import gcd
print(gcd(12, 18))