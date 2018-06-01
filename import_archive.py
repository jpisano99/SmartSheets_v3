__author__ = 'jpisano'


import MySQLdb as mysql
from my_functions import table_exists
from settings import app,database
from my_functions import csv_from_excel,stamp_it

#
#
#
def import_archive():
    # This is to import an entire Fiscal Year of Data
    cnx = mysql.connect(user=database['USER'], passwd=database['PASSWORD'], host=database['HOST'], db=database['DATABASE'])
    mycursor = cnx.cursor()

    working_dir = app['WORKING_DIR']
    working_file = app['ARCHIVE_FILE']
    working_csv_file = app['ARCHIVE_CSV_FILE']
    working_data_dir = app['WORKING_DATA_DIR']
    as_of_date = app['AS_OF_DATE']


    #Convert xls bookings file to CVS
    print("\tProcessing FY17 Archive Bookings Data...")
    csv_from_excel(working_dir+working_data_dir+working_file,'Data')
    #Stamp it and save it
    stamp_it(working_dir + working_data_dir + working_file, as_of_date)
    #CSV file now prepped.


    #Clean up existing archive if it exists
    if table_exists(mycursor,'archive_bookings_data_fy17'):
        sql = "DROP TABLE archive_bookings_data_fy17"
        mycursor.execute(sql)
        print("Deleted FY17 Archive Bookings Data...")
        cnx.commit()

    #Create new archive bookings table
    #
    sql = ('CREATE TABLE archive_bookings_data_fy17 '
        '(`Fiscal Year` TEXT,'
        '`Fiscal Quarter ID` TEXT,'
        '`Fiscal Period ID` TEXT,'
        '`Fiscal Week ID` TEXT,'
        '`Date Booked` DATE,'
        '`Sales Level 1` TEXT,'
        '`Sales Level 2` TEXT,'
        '`Sales Level 3` TEXT,'
        '`Sales Level 4` TEXT,'
        '`Sales Level 5` TEXT,'
        '`Sales Level 6` TEXT,'
        '`Sales Agent Name` TEXT,'
        '`Internal Business Entity Name` TEXT,'
        '`Internal Sub Business Entity Name` TEXT,'
        '`Product Family` TEXT,'
        '`Product ID` TEXT,'
        '`End Customer Global Ultimate Name` TEXT,'
        '`End Customer Global Ultimate Company Target ID` TEXT,'
        '`Ship to ERP Customer Name` TEXT,'
        '`Sales Order Number Detail` TEXT,'
        '`ERP Deal ID` TEXT,'
        '`Corporate Bookings Flag` TEXT,'
        '`Partner Name` TEXT,'
        '`SCMS` TEXT,'
        '`Product Bookings Net` TEXT,'
        '`Service Bookings Net` TEXT,'
        '`Bookings Adjustments Description` TEXT ,'
        '`Hash Value` VARCHAR (32)) ')

    mycursor.execute(sql)
    cnx.commit()

    #Add an index to speed customer lookups
    sql= ("ALTER TABLE  `archive_bookings_data_fy17` "
                "ADD INDEX `cust` (`End Customer Global Ultimate Name`(75) ASC)")
    mycursor.execute(sql)
    cnx.commit()

    print("Importing FY17 Archive Bookings Data...")
    sql = ("load data local infile '" + working_dir+working_data_dir + working_csv_file + "' into table archive_bookings_data_fy17 "
            "fields terminated by ',' "
            "enclosed by '\"' "
            "escaped by '' "
            "lines terminated by '\r\n' "
            "ignore 1 lines")
    mycursor.execute(sql)
    cnx.commit()
    cnx.close()


if __name__ == "__main__":
    import_archive()