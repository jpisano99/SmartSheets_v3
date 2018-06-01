__author__ = 'jpisano'
import smartsheet
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "test" Sheet ID
row_id = '4542989902079876'  # row number 4
customer_col='4113607471458180'  # Customer name

row = ss.Sheets.get_row(sheet_id,row_id, include='discussions,attachments,columns,columnType')

for cell in row.cells:
    print(cell.column_id, cell.column_type, cell.value)

    # Get the row as a dict
    cell_dict = cell.to_dict()
    # print('dict: ', cell_dict)
    # print(row_dict['columnType'])
