import math
def route(d):
    a,b = len(d), len(d[0])
    r = ()
    def req(x, y):
        if (x, y) in r: return r[x,y]
        if x == 0 and y == 0:
            r[0,0] = d[0][0]
            return r[0,0]
        if x < 0 or y < 0: return math.inf
        r[x,y] = d[x][y] + min(req(x-1, y), req(x, y-1))
        return r[x,y]
    min_path = req(a-1, b-1)
    for i in range(a):
        print(*(r[i,j] for j in range(b)))
    return min_path
d = [[10, 1, 1, 1, 1, 1],
     [5, 20, 20, 20, 1, 1],
     [10, 1, 1, 1, 1, 1],
     [90, 1, 20, 20, 1, 5],
     [5, 1, 1, 1, 1, 1]]
print(f"(route(d)=)")

