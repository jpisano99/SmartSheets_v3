__author__ = 'jpisano'
import smartsheet
import ast
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "test" Sheet ID
row_id = '4542989902079876'  # row number 4
customer_col='4113607471458180'  # Customer name

row = ss.Sheets.get_row(sheet_id,row_id, include='discussions,attachments,columns,columnType')
#print(row)

for cell in row.cells:
    print(help(cell))
    print (cell.column_id,cell.column_type,cell.value)

    jim = cell.to_dict()
    #print (cell)
    #ang = ast.literal_eval(jim) #
    print('dict: ',jim)
    print (jim['columnType'])
    exit()