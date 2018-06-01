__author__ = 'jpisano'
import requests
import json
from settings import smartsheet

my_token  = smartsheet['SMARTSHEET_TOKEN']

sheetid ='4816554870237060'  # "test" Sheet ID
rowid='4542989902079876'  # row number 4
customer_col='4113607471458180'  # Customer name

my_token  = smartsheet['SMARTSHEET_TOKEN']
url = 'https://api.smartsheet.com/2.0/sheets/' + sheetid +'/rows/' + rowid
myheader = {'Authorization': 'Bearer '+ my_token}

response = requests.get (url,headers=myheader)
data = json.loads(response.text)
row = data["rowNumber"]
cells = data["cells"]

for cell in cells:
    if str(cell["columnId"]) in customer_col:
        print ("Customer Name: ",row,cell["value"],cell["value"],cell["columnId"],customer_col)
