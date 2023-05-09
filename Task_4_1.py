def calc():
    while True:
        x = input("Введите нужную операцию в формате 1 + 2. Для отмены введите 0. ")
        if x == "0":
            break
        print(x + " = " + str(eval(x)))
calc()