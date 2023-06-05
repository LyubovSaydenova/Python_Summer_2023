import re
string = "A123BC78, X666XX178"
a = "AАBВCСXХYУ"
regex = rf"[{a}]\d\d\d[{a}][{a}][1]?78"
print(re.findall(regex, string))