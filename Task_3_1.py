list = []
while True:
    n = int(input("Зарплата = "))
    if n == 0: break
    list.append(n)
print("Средняя зарплата =", sum(list)/len(list))


