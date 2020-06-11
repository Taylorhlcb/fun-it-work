# Program to extract a particular row value
import xlrd
import json

loc = ("pdf1.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
csv_list = []
for row in range(1,23):
    print("Row number: " + str(row))
    print(sheet.row_values(row))
    csv_list.append(sheet.row_values(row))
print(csv_list)
with open('exported-csv.json', 'w') as f:
    json.dump(csv_list, f, indent=2)
