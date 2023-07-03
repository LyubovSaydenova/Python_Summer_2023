def cmpr(s, z):
    if abs(len(s) - len(z)) > 1: return False
    if s in z or z in s: return True
    if len(s) != len(z): return False
    if sum([s[i] != z[i] for i in range(len(s))]) > 1: return False
    return True
while True:
    s = input()
    z = input()
    print(cmpr(s, z))