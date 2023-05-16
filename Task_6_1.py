d = {'CM':900, 'M':1000, 'CD':400, 'D':500, 'C':100, 'XL':40, 'L':50, 'IX':9, 'X':10, 'IV':4, 'V':5, 'I':1}
s = input()
res = 0
while True:
    if not s: break
    for k, v in d.items():
        if s.startswith(k):
            res += v
            s = s[len(k):]
            break
    print(f'{res=} {s=}')
print(res)