import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",     # localhost
        user="vsearch",
        password="vsearchpasswd",
        database="vsearchlogDB"
    )
    with conn.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        res = cursor.fetchall()
        print(res)
finally:
    if 'conn' in locals():
        conn.close()
