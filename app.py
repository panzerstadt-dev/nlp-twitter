import xlrd
import csv
import os.path as path

xls_filepath = './data/temp.xls'

def csv_from_excel():
    workbook = xlrd.open_workbook(xls_filepath)
    worksheet = workbook.sheet_by_name('Sheet1')
    print(worksheet.)
    csv_output = open(''.join([path.basename(xls_filepath), '.csv']), 'wb')
    write = csv.writer(csv_output, delimiter='|')

    for rownum in range(worksheet.nrows):
        write.writerow(worksheet.row_values(rownum))
    csv_output.close()

csv_from_excel()