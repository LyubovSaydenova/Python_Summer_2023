x = ["abab", "xa", "ax", "aaaaaaaa", "abcbab"]
print(sorted(x, key = lambda y: (-len(set(y)), y)))