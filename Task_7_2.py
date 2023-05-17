def ceasar(string, n):
    res = ""
    n26 = n % 26
    for i in string:
        if "a" <= i <= "z":
            new_i = ord(i) + n26
            if new_i > ord("z"):
                new_i = ord("a") + new_i - ord("z") - 1
            res += chr(new_i)
        return res
print(ceasar("abcxyz", 54))