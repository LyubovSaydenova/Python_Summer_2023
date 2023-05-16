s1 = input()
s2 = input()
print(*(set(s1.split()) & set(s2.split())))