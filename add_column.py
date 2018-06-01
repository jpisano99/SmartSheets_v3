__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "cust_ref_ent" Sheet ID

# Create the columns
column1 = ss.models.Column({
  'title': 'New Picklist Column 1',
  'type': 'PICKLIST',
  'options': [
    'First',
    'Second',
    'Third'
  ],
  'index': 4
})

column2 = ss.models.Column({
  'title': 'New Date Column',
  'type': 'DATE',
  'index': 4
})

# Add columns to the sheet
new_columns = ss.Sheets.add_columns(sheet_id, [column1, column2])

