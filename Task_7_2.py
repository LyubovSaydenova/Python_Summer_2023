a = int(input())
b = input()
c = '!?., '
def coder():
    for i in b:
        if i in c:
            print(chr(ord(i)), end='')
        if i.islower():
            if ord(i) + a > 122:
                print(chr(ord(i) + a - 26), end='')
            else:
                print(chr(ord(i) + a), end='')
        elif i.isupper():
            if ord(i) + a > 90:
                print(chr(ord(i) + a - 26), end='')
            else:
                print(chr(ord(i) + a), end='')
    print()
coder()