n = int(input("n = "))
a = [[0] * n for i in range(n)]
count = 0
for i in range(n):
    count += 1
    a[0][i] = count
j = 0
i = n-1
n -= 1
while len(a)**2 != count:
    for k in range(n):
        j += 1
        count += 1
        a[j][i] = count
    for k in range(n):
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        i += 1
        count += 1
        a[j][i] = count
    n -= 2
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()