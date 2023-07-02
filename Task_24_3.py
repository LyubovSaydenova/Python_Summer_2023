def braces(s):
    d = {'(':1, ')':-1}
    r = 0
    for i in s:
        r += d[i]
        if r < 0: return False
    return r == 0
while True:
    print(braces(input()))