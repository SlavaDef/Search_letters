from functools import wraps

from flask import session


def checker_loger_in(func):
    """Check if user is logged in"""
    # Використовується декоратор `@wraps(func)` з модуля  `functools`,
    # який зберігає метадані оригінальної функції (назву, докстрінги тощо)
    @wraps(func)
    def wrapper(*args, **kwargs):

        if 'logged_in' in session: # - Перевіряється чи є ключ 'logged_in' в об'єкті `session` (це Flask сесія)
            return func(*args, **kwargs)  # Якщо користувач залогінений - виконується оригінальна функція тобто моя ретурн page1

        return 'You are not logged in' # - Якщо ні - повертається повідомлення про помилку


    return wrapper
