def pal():
    n = 0
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            yield n
gen = pal()
for _ in range(int(input())):
    print(next(gen), end = ' ')