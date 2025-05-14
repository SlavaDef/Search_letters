from flask import Flask, session
from decorators.checker import checker_loger_in

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/page1')
@checker_loger_in # імпортуємо наш декоратор і прикріплюємо до сторінок у яких повинен бути обмежаний доступ
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
@checker_loger_in
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
@checker_loger_in
def page3() -> str:
    return 'This is page 3.'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') #  видалення з словника
    return 'You are now logged out.'





app.secret_key = 'YouWillNeverGuessMySecretKey'



if __name__ == '__main__':
 app.run(debug=True)