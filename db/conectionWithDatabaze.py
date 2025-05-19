import pymysql

from Exeptions.myExeptions import CredentialsError, SQLError, DatabaseConnectionError


class UseDatabase:
    def __init__(self, **config):
        self.config = config
        self.conn = None
        self.cursor = None


    def __enter__(self): # авто визов у блоці with
        try:
            self.conn = pymysql.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except pymysql.Error as e:
            raise Exception(f"Помилка бази даних: {e}")
        except pymysql.ProgrammingError as err:
            raise CredentialsError(err)


    def __exit__(self, exc_type, exc_value, exc_trace):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                if exc_type is None:
                    self.conn.commit()
                else:
                    self.conn.rollback()
                self.conn.close()
        except pymysql.Error as e:
            raise DatabaseConnectionError(f"Помилка при закритті з'єднання: {e}", e)

        if exc_type:
            if isinstance(exc_value, pymysql.ProgrammingError):
                # Помилки синтаксису SQL
                raise SQLError(f"Помилка в SQL запиті: {exc_value}", exc_value)
            elif isinstance(exc_value, pymysql.OperationalError):
                # Помилки роботи з базою даних
                raise DatabaseConnectionError(f"Помилка операції з БД: {exc_value}", exc_value)
            elif isinstance(exc_value, pymysql.InternalError):
                # Внутрішні помилки MySQL
                raise SQLError(f"Внутрішня помилка MySQL: {exc_value}", exc_value)
            elif isinstance(exc_value, pymysql.Error):
                # Інші помилки MySQL
                raise DatabaseConnectionError(f"Помилка бази даних: {exc_value}", exc_value)

        return True

#  Методи `__enter__` та `__exit__` - це спеціальні методи Python,
# які виконуються автоматично при використанні контекстного менеджера (конструкції `with`). Ось як це працює:

# 1. Коли ви використовуєте конструкцію `with`, Python автоматично:
#     - Викликає метод `__enter__` на початку блоку `with`
#     - Викликає метод `__exit__` при виході з блоку `with`

# Наприклад, коли ви пишете:
# ``` python
# with UseDatabase(**dbconfig) as cursor:
#     # ваш код
# ```
# За лаштунками відбувається наступне:
# ``` python
# # 1. Створюється екземпляр класу
# db = UseDatabase(**dbconfig)
#
# # 2. Автоматично викликається __enter__
# cursor = db.__enter__()
#
# try:
#     # 3. Виконується ваш код всередині блоку with
#     # ...
# finally:
#     # 4. Автоматично викликається __exit__ при виході з блоку
#     db.__exit__(exc_type, exc_value, traceback)
# ```
# Це дуже корисний патерн, тому що:
# 1. Гарантує звільнення ресурсів (закриття з'єднань, файлів тощо)
# 2. Автоматично обробляє помилки
# 3. Робить код чистішим та безпечнішим