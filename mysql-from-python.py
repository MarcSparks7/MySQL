import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:34")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()