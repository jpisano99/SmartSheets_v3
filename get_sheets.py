__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token=smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

response = ss.Sheets.list_sheets(include_all=True)
sheets = response.data

for sheet in sheets:
    print(sheet.id, sheet.name, sheet.permalink)

