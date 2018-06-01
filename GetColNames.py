__author__ = 'jpisano'
import requests
import json
from settings import smartsheet

my_token  = smartsheet['SMARTSHEET_TOKEN']
sheetid ='4816554870237060'  # "test" Sheet ID
url = 'https://api.smartsheet.com/2.0/sheets/' + sheetid

myheader = {'Authorization': 'Bearer '+ my_token}

response = requests.get (url, headers = myheader)
data = json.loads(response.text)
columns = data["columns"]
columnDict = {}

for column in columns:
    print (column["id"]," >> ",column["title"])
    columnDict.update({column ["id"]: column["title"]})

for column,name in columnDict.items():
    print (column,name)



