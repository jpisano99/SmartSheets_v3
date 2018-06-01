__author__ = 'jpisano'
from datetime import datetime
from my_secrets import passwords

#database configuration settings
database = dict(
    DATABASE = "cust_ref_db",
    USER     = "root",
    PASSWORD = passwords["DB_PASSWORD"],
    HOST     = "localhost"
)

#Smartsheet Config settings
smartsheet_conf = dict(
    SMARTSHEET_TOKEN=passwords["SMARTSHEET_TOKEN"],
    SHEET_NAME="Test Sheet"
)

#application predefined constants
app = dict(
    VERSION   = 1.0,
    GITHUB    = "{url}",
    #DOWNLOAD_FILE='Daily_Bookings_Nexus_9K-91007-test.zip',
    DOWNLOAD_FILE = 'Daily_Bookings_Nexus_9K-91007.zip',
    DOWNLOAD_DIR = 'c:/users/jpisano/downloads/',
    WORKING_DIR = 'c:/users/jpisano/desktop/ACI to Production Database - Beta/',
    WORKING_FILE = 'Daily_Bookings_Nexus_9K.xlsm',
    WORKING_CSV_FILE = 'Daily_Bookings_Nexus_9K.csv',
    WORKING_DATA_DIR = 'todays_bookings_data/',
    ARCHIVE_FILE='fy17_data.xlsm',
    ARCHIVE_CSV_FILE='fy17_data.csv',
    AS_OF_DATE = datetime.now().strftime('_as_of_%m_%d_%Y')
)

