__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "test" Sheet ID
col_id1 = 4113607471458180   # Customer name
col_id2 = 1580332681062276   # Assigned PSS

# Create Row Object(s)

# Specify cell values for a row (row_a)
row_a = ss.models.Row()

row_a.to_top = True
row_a.cells.append({
  'column_id': col_id1,
  'value': True
})

row_a.cells.append({
  'column_id': col_id2,
  'value': 'New Status',
  'strict': False
})

# Specify cell values for another row (row_b)
row_b = ss.models.Row()
row_b.to_top = True
row_b.cells.append({
  'column_id': col_id1,
  'value': True
})
row_b.cells.append({
  'column_id': col_id2,
  'value': 'New Status',
  'strict': False
})

# Add rows to sheet
response = ss.Sheets.add_rows(sheet_id,[row_a, row_b])
