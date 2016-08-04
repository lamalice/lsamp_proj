__author__ = 'Alice'
#!/usr/bin/python3

import pymysql
#import is successful

db = pymysql.connect(host = 'mysql.cis.ksu.edu', user = 'lamalice16', password = 'Bluedafs!1234', db = 'proj_lsamp')
#logging into mysql server

cursor = db.cursor()
#delcaring a  cursor
cursor.execute('Select Version()')
data = cursor.fetchone()
#fetching one line from the database
print('Database version: %s ', data)
#a test to see if the connection was open

def queryloop(i,j):
    for i in range(1,70):
        for j in range(1, i-1):
            print(i,j)
#function that loops through all cows in the query syntax

db.close()
