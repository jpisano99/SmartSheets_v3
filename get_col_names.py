__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheetid = '4816554870237060'  # "test" Sheet ID

sheet = ss.Sheets.get_sheet(sheetid)

columns = sheet.columns

for column in columns:
    print(sheet.name,column.title,column.id)




