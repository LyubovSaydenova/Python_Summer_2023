s = [1, 2, [11, 22, [111, 222, [1111, 2222, 3333], 333]]]
r = []
def rec_list(z):
    for i in z:
        if type(i) == list:
            rec_list(i)
        else:
            r.append(i)
rec_list(s)
print(len(r))