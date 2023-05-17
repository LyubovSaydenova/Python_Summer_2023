def max3(matrix):
    list = []
    for i in matrix:
        for j in i:
            list.append(j)
    return sorted(sorted(list, reverse = True) [:3])
print(max3([[111, 200], [22, 2, 3, 400, 5], [100]]))