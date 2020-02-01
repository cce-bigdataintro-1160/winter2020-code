#!/usr/bin/env python3

import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server};Server=cebd1160-sqlserver.database.windows.net;Uid=elomonaco;Pwd='H7g27@QNgnx@';")
cnxn = pyodbc.connect('Server=cebd1160-sqlserver.database.windows.net;User ID=elomonaco;Password=H7g27@QNgnx@')

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM SalesLT.Customer')

for row in cursor:
    print('row = %r' % (row,))