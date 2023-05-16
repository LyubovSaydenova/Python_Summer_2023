def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return a // gcd(a, b) * b
n = int(input('Количество чисел: '))
numbers = []
for i in range(n):
    numbers.append(int(input('n_{0}: '.format(i))))
res = lcm(numbers[0], numbers[1])
for i in range(2, n):
    res = lcm(res, numbers[i])
print(res)