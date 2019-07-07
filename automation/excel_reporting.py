import xlrd

excelFile1 = 'excel1.xlsx'
excelFile2 = 'excel2.xlsx'

book1 = xlrd.open_workbook(excelFile1)
book2 = xlrd.open_workbook(excelFile2)

first_sheet = book1.sheet_by_index(0)
second_sheet = book2.sheet_by_index(0)