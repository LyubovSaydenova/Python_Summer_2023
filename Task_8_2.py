numbers = [[1, 5, 3], [2, 44, 1, 4], [4, 9, 4, 5], [3, 4], [4444], [55], [333]]
print((sorted(numbers, key=lambda j: (len("".join(map(str, j))), j.sort(key=lambda k: -k)))))