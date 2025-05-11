

def write_db(phrase, letters, remote_addr, user_agent, res):
    import pymysql

    from utils.constants import dbconfig, SQL3

    try:
        conn = pymysql.connect(**dbconfig)  # створення конекшену

        #cursor = conn.cursor()
        with conn.cursor() as cursor:
             cursor.execute(SQL3, (phrase, letters, remote_addr, user_agent, res))  # кортедж данних
             conn.commit()  # збереження данних

    finally:
       if 'conn' in locals():
           conn.close()


# виконує запит до бд і повертає всі поля
def read_all_from_db():
    import pymysql

    from utils.constants import dbconfig, SQl4

    try:
        conn = pymysql.connect(**dbconfig)  # створення конекшену

        #cursor = conn.cursor()
        with conn.cursor() as cursor:
             cursor.execute(SQl4)
             conn.commit()

    finally:
        conn.close()

    return cursor.fetchall()


#print(read_all_from_db())