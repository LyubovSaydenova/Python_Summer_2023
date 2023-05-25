import csv
with open ("test.csv", encoding="utf-8")
    rows = csv.DictReader(fi)
    su = 0
    for row in rows:
        su += int(row["salary"])
import openpyxl
from openpyxl import Workbook
wb = Workbook()
wb.save("result.xlsx")
pd.test.csv("test.csv", sep=",", encoding="utf-8").to_excel("result.xlsx", index=None))
print(f"ИТОГО: {su}")