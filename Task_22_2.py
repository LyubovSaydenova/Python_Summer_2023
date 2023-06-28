tree = [(1,2),(1,3),(3,4),(4,5),(5,6),(6,7),(7,8)]
d = {1:0}
for i, j in tree:
    d[j] = d[i] + 1
print(max(d.values()))