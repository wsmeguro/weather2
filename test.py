import os,sys

sys.path.append('/home/masuday/tools/py-env3')

import mysql.connector as mydb

conn = mydb.connect(host='localhost', user='masuday_tools',
                    password='Kurodai', database='masuday_tools')
curs = conn.cursor()

sql= "INSERT IGNORE INTO tbl_test (date1, intA, strA, floatA, doubleA) VALUES ('%s', %d, '%s', %f, %f)"
date1='2023-3-15'
intA=12
stringA='やっぱりテストです'
floatA=1.2345
doubleA=1234.56789
print(sql %(date1, intA, stringA, floatA, doubleA))
curs.execute(sql %(date1, intA, stringA, floatA, doubleA))
conn.commit()

curs.close()
conn.close()