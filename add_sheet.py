__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token=smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_spec = ss.models.Sheet({
  'name': 'newsheet',
  'columns': [{
      'title': 'Favorite',
      'type': 'CHECKBOX',
      'symbol': 'STAR'
    }, {
      'title': 'Primary Column',
      'primary': True,
      'type': 'TEXT_NUMBER'
    }
  ]
})
response = ss.Home.create_sheet(sheet_spec)
new_sheet = response.result

print(type(new_sheet))
print(dir(new_sheet))

print(new_sheet)


