import re
n = int(input())
x, y = divmod(n, 10)
if x == 1 and y == 0:
    regex = rf'(?<![-])\b\d\b|\b(?<![-])10\b'
elif x > 1 and y == 0:
    regex = rf'(?<![-])\b\d\b|(?<![-])\b[1-{x-1}]\d\b|(?<![-])\b{x}0\b'
elif x > 1 and y > 0:
    regex = rf'(?<![-])\b\d\b|(?<![-])\b[1-{x-1}]\d\b|(?<![-])\b{x}[0-{y}]\b'
elif x == 1 and y > 0:
    regex = rf'(?<![-])\b\d\b|(?<![-])\b1[0-{y}]\b'
print(*re.findall(regex, str(list(range(-200, 200)))))