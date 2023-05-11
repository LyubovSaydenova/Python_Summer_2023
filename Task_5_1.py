z={}
n = int(input())
for i in range(n):
    y=[1]
    for k in range(1,i):
        y.append(int(z[i-1][k-1])+int(z[i-1][k]))
    if i>0:
        y+=[1]
    z[i]=y
for k,v in z.items():
    print(k,v)