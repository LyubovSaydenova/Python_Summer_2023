s = input()
z = ""
i = 0
while True:
    if s[i:i+2] == "АГ":
        z += "ГА"
        i += 2
    elif s[i:i+2] == "ЦТ":
        z += "ЦАГТ"
        i += 2
    else:
        z += s[i]
        i += 1
    if i >= len(s) - 1: break
print(z)