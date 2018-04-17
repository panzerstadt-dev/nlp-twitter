import xlrd
import csv
import os.path as path
from os import mkdir


xls_filepath = './raw_data/temp.xls'
jp_filepath = './raw_data/10000_tweets.xls'

def csv_from_excel(input_filepath=xls_filepath, debug=False, new_folder='processed'):

    workbook = xlrd.open_workbook(input_filepath)
    worksheet = workbook.sheet_by_index(0)

    if debug:
        sh = worksheet
        print("sheet name: {0}, rows: {1}, columns: {2}".format(sh.name, sh.nrows, sh.ncols))
        print("example: Cell D30 is --> {0}".format(sh.cell_value(rowx=29, colx=3)))

    new_basename = path.basename(input_filepath)
    new_filename = ''.join([path.splitext(new_basename)[0], '.tsv'])

    if new_folder:
        if not path.isdir(new_folder):
            print('making new folder called {0}'.format(new_folder))
            mkdir(new_folder)

        new_filename = path.join(new_folder, new_filename)

    csv_output = open(new_filename, 'w')

    print('using \\t (tab) as delimiter')
    write = csv.writer(csv_output, delimiter='\t')

    for rownum in range(worksheet.nrows):
        worksheet_row = worksheet.row_values(rownum)

        if debug:
            print('showing example rows')
            if rownum <= 10:
                print(worksheet_row)

        worksheet_row = [str(w_row).replace('\n', ' ') for w_row in worksheet_row]
        write.writerow(worksheet_row)
    csv_output.close()


csv_from_excel(xls_filepath)

