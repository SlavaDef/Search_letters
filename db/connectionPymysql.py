import pymysql

from utils.constants import dbconfig, SQL3, SQL4

conn = pymysql.connect(**dbconfig) # створення конекшену


cursor = conn.cursor()

#cursor.execute(_SQL3,  ('reniman', 'n', '127.0.0.1', 'Opera', '{n}')) # кортедж данних
#conn.commit() # збереження данних



cursor.execute(SQL4)

for row in cursor.fetchall():
    print(row)
    # print(row[0]) = id
    # print(row[6]) = res


cursor.close()
conn.close()







#res = cursor.fetchall()# список кортежів стовпців
#print(res)

#for row in res:
    #print(row)