s = input()
def maska(x): # эта функция выдаёт по слову маску
    res = []
    for i, j in enumerate(x):
        if j in "ауоыиэяюёе": # гласные определять тем, что выписать все гласные буквы алфавита
            res.append(i)
        return res
print(maska(s))
out = []
z = input().split()
for i in z:
    if maska(i) == maska(s):
        out.append(i)
print(*out)