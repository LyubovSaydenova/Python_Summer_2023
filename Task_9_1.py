d = {"G":"C", "C":"G", "T":"A", "A":"T"}
dnk = input()
rnk = ""
for i in dnk:
    rnk += d[i]
print(rnk)