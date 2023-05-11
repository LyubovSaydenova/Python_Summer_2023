d = int(input())
for i in range(d - 1, 1, -1):
    n = 0
    if (d % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                n = n + 1
        if (n == 0):
            print(i, end = " ")