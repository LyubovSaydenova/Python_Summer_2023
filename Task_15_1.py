dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
x = 1
for k, v in dct.items():
    if k == x:
        print(v)
    if type(v) == dict:
        for p, q in v.items():
            if p == x:
                print(q)