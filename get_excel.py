__author__ = 'jpisano'

import smartsheet
import os
from settings import smartsheet_conf

ss_token = smartsheet_conf['SMARTSHEET_TOKEN']
ss = smartsheet.Smartsheet(ss_token)

sheet_id = '4816554870237060'  # "cust_ref_ent" Sheet ID

ss.Sheets.get_sheet_as_excel(sheet_id, os.path.abspath('c:/users/jim/desktop'))
