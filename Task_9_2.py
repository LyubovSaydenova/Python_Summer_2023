s = input()
def maska(x):
    res = []
    for i, j in enumerate(x):
        if j in "ауоыиэяюёе":
            res.append(i)
        return res
print(maska(s))
out = []
z = input().split()
for i in z:
    if maska(i) == maska(s):
        out.append(i)
print(*out)