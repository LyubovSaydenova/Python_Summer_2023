list = [33, 12, 7, 19, 55]
print(list)
a = list[0] if list else None
for i in list:
    if i<a:
        a=i
print(f"Наименьшее число из списка = {a}")