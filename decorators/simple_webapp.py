import os

from flask import Flask, session, render_template, request
from decorators.checker import checker_loger_in
from service.write import reading_log_file
from utils.constants import file_from_pc

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'webapp'))

app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

app.secret_key = reading_log_file(file_from_pc)


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


#@app.route('/login')
#def do_login() -> str:
   # session['logged_in'] = True
    #return 'You are now logged in.'



@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') #  видалення з словника
    return 'You are now logged out.'


@app.route('/login', methods=['GET', 'POST'])
def do_login():
    title = "Please log in to see this pages"
    if request.method == 'POST':
        secret_code = request.form.get('secret_code')
        phrase = "Incorrect secret code. Please try again."

        if secret_code == app.secret_key:  # перевірка введеного коду
            session['logged_in'] = True
            return 'Ви успішно увійшли'
        else:
            return render_template('login.html', the_phrase = phrase)
    return render_template('login.html', the_title = title)  # сторінка з формою




#Якщо ви спробуєте прибрати рядок `app.secret_key = 'YouWillNeverGuessMySecretKey'`,
# то отримаєте помилку `RuntimeError: The session is unavailable because no secret key was set`.
# Це тому що Flask не дозволить працювати з сесіями без встановленого секретного ключа.
# Тобто хоча ви не викликаєте `secret_key` напряму, він використовується "за лаштунками"
# кожного разу, коли ви працюєте з об'єктом `session`.









if __name__ == '__main__':
 app.run(debug=True)