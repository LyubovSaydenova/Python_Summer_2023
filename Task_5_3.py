n = int(input())
for i in range(1, n):
    f = int((((1+5**0.5)/2) ** i - ((1-5**0.5)/2) ** i) / 5**0.5)
    print(f)