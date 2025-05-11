import pymysql

from db.conectionWithDatabaze import UseDatabase
from utils.constants import  SQL3, SQL4, dbconfig


def write_db(phrase, letters, remote_addr, user_agent, res):


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

    try:
        conn = pymysql.connect(**dbconfig)  # створення конекшену

        #cursor = conn.cursor()
        with conn.cursor() as cursor:
             cursor.execute(SQL4)
             conn.commit()

    finally:
        conn.close()

    return cursor.fetchall()


def read_all_from_db2():

    try:
        with UseDatabase(**dbconfig) as cursor:
            cursor.execute(SQL4)
            res = cursor.fetchall()
            return res

    except Exception as e:
        print(f"Помилка: {e}")
        return []




#print(read_all_from_db2())