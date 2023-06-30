max_ = None
site_ = 0
for i in range(1, int(input())+1):
    num = int(input())
    if num ** 2 < 1000 and max_:
        if num > max_:
            max_ = num
            site_ = i
    elif not max_ and num ** 2 < 1000:
        max_ = num
        site_ = i
print(max_, site_)