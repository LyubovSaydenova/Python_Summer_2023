x = int(133244459)
s = str(x)
for i in range(10):
    si = str(i)
    print(f"{si} - {s.count(si)}")