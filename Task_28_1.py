arr = []
res = 0
for _ in range(int(input())):
    n = int(input())
    res += sum(el > n for el in arr)
    arr.append(n)
print(res)