import pymysql

from Exeptions.myExeptions import CredentialsError, SQLError
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


def read_from_db(sql) -> list:

    try:
        with UseDatabase(**dbconfig) as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
    except CredentialsError as err: # власні виключення які виникають завдяки припису в методі __exit__ конекшену до бд
        print('User-id/Password issues. Error:', str(err))
        return []
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
        return []
    except SQLError as err:
        print('Is your sql is correct?', str(err))
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []




#print(read_from_db("SELECT * FROMM users"))