def f(num, a=0):
    return f(num // 10, a + 1) if num else a
print(f(int(input())))

