import re
s = input()
print(re.sub(r'\b\w+\b', lambda x:x.group().upper()[0], s).replace(' ', ''))