s = input()
import re
print(re.sub(r"(\b\w+\b)\W+\b\1\b", r"\1", s))