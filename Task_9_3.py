from collections import Counter
d = Counter(input())
b = dict(d)
s = sorted(b.items(), key = lambda x: (-x[1], x[0]))
for i,j in s[:10]:
    print(f"{i} - {j}")