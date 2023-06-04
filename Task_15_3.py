import re
string = "+7(812)333-4444, +7(812)333-44-44, +7(921)333-4444, +7(921)333-44-44"
regex = r'\S\d\S\d{3}\S\d{3}\S\d{4}|\S\d\S\d{3}\S\d{3}\S\d{2}\S\d{2}'
print(re.findall(regex, string))