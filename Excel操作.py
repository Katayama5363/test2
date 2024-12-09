import openpyxl as px
import random as hhhh


wb = px.Workbook()

sheet = wb.active
total = 0
for m in range(2,501):
    random_value = hhhh.randint(1,1000000)
    sheet["A"+ str(m)] = random_value
    total +=random_value
sheet["B"+ str(1)] = total
wb.save("example0.xlsx")