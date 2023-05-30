t = list(map(int, input().split()))
for i in enumerate(t):
    if i % 2 != 0:
        print(i, sep = ', ')