s = list(map(int, input().split()))
print([s[i] for i in range(1, len(s)) if s[i-1] + 1 != s[i]])