import pymysql
from DB_API.rows import Rows

conn = pymysql.connect(host='localhost', port=33060, user='homestead', password='secret', db='clients')
cursor = conn.cursor()

cursor.execute(Rows.get_all("courson_courses"))

row = cursor.fetchone()
all_rows = cursor.fetchall()
print(row)
print('\n-------------------------------------------')
print(cursor.rowcount)
print('\n-------------------------------------------')
print(all_rows)

conn.close()
