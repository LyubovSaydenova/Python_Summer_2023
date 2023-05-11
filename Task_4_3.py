s = input()
z = input()
d = {}
t = {}
ab = "abcdefghijklmnopqrstuvwxyz"
ab1 = "абвгдеёжзийклмнопрстуфцчшщэюя"
for i in s:
    il = i.lower()
    if il in ab or il in ab1:
        d[il] = d.get(il, 0) + 1
for i in z:
    print(d == t)