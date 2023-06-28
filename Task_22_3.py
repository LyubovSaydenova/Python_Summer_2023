s = input()
import keyword
for i in keyword.kwlist:
    s = s.replace(i, '<kw>')
print(s)