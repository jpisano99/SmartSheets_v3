__author__ = 'jpisano'

import MySQLdb as mysql
from settings import database

cnx = mysql.connect(user='root', passwd=database['PASSWORD'], host='localhost', db='cust_ref_db')
mycursor = cnx.cursor()

cnx1 = mysql.connect(user='root', passwd=database['PASSWORD'], host='localhost', db='cust_ref_db')
mycursor1 = cnx1.cursor()

path_to_import = 'c:/users/jpisano/desktop/ACI to Production Database/Todays Data/'
file_to_import = 'fy16_bookings_data.csv'
