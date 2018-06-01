__author__ = 'jpisano'

import smartsheet
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "test" Sheet ID
row_id = '4542989902079876'  # row number 4
customer_col = '4113607471458180'  # Customer name

url = 'https://api.smartsheet.com/2.0/sheets/' + sheet_id + '/columns'
my_header = {'Authorization': 'Bearer '+ ss_token, 'Content-Type': 'application/json'}

response = requests.post (url,headers=myheader,json={"index": "5", "title": "my1stcol", "type": "TEXT_NUMBER"})
print (response.url)
print (response.content)
data = json.loads(response.text)
