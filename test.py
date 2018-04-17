import xlrd
book = xlrd.open_workbook("./data/temp.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("sheet name: {0}, rows: {1}, columns: {2}".format(sh.name, sh.nrows, sh.ncols))
print("example: Cell D30 is --> {0}".format(sh.cell_value(rowx=29, colx=3)))


# for rx in range(sh.nrows):
#     print(sh.row(rx))