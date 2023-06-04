import re
string = "A123BC78, X666XX178"
regex = r"\b\w\d{3}\w{2}\d{2-3}\b"
print(re.findall(regex, string))