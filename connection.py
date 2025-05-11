import mysql.connector


#dbconfig = {'host': '127.0.0.1',
  #          'user': 'vsearch',
   #         'password': 'vsearchpasswd',
   #         'database': 'vsearchlogDB', }

#conn = mysql.connector.connect(**dbconfig) # створення конекшену
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="vsearch",
        password="vsearchpasswd",
        database="vsearchlogDB"
    )
except mysql.connector.Error as err:
       print(f"Помилка: {err}")


if __name__ == '__main__':
    cursor = conn.cursor()
    #_SQL = """show tables"""
    cursor.execute("SHOW TABLES")
    res = cursor.fetchall()
    print(res)