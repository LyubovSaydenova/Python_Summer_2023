s = input("Предложение из нескольких слов - ")
list = s.split()
x = 0
for i in list:
    if len(i) > x:
        x = len(i)
for i in list:
    if len(i) == x:
        print(i)