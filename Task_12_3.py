s = [p.split('-') for p in input().split(',')]
print([k for p in s for k in range(int(p[0]), int(p[1])+1)])