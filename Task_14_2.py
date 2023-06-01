def fun(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return fun(num, res)
print(fun(int(input())))
