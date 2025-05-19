import html
import os

from  flask import Flask, render_template, request, session
from werkzeug.utils import redirect
from user_agents import parse

from decorators.checker import checker_loger_in
from service.dbWrite import write_db, read_from_db
from service.logs import  view_logs3, view_the_logs2
from service.privat import get_exchange_rates, get_exchange
from service.search_letters import find_letters_in_words_ai
from threading import Thread


from service.write import  write_message, log_request, reading_log_file
from utils.constants import file_from_pc, SQL4

# Отримаємо абсолютний шлях до каталогу webapp/
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'webapp'))

app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

#@app.route('/')
#def hello() -> '302':
  #  return redirect('/entry')


#app.config['dbconfig'] = {'host': '127.0.0.1','user': 'vsearch','password': 'vsearchpasswd','database': 'vsearchlogDB', }

app.secret_key = reading_log_file(file_from_pc)

@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    remote = str(request.remote_addr)

    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    browser = user_agent.browser.family

    title = 'Here are you results'
    results = str(find_letters_in_words_ai(phrase,letters))

    write_db(phrase, letters, remote, browser, results)
    currency_res = get_exchange_rates() # курси валют
    write_message(phrase, letters, results) # запис  данних про вводи, my wersion
    try:
        # запуск методу в окремому потоці, підстраховка якщо запит виконується довго але потрібно перенести сюди метод
        # для коректної роботи
        #t = Thread(target=log_request, args=(request, results))
       # t.start()
        log_request(request,results) # book version
    except Exception as err:
        print('Loding file with this error - ',str(err))

    return render_template('results.html', the_phrase = phrase, the_letters = letters,
                           the_title = title, the_results= results, the_currency_res = currency_res )



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')




@app.route('/privat')
def get_exchange_rates() -> html:
     return render_template('privat.html', the_title = 'Exchange_rates', pr_data=get_exchange())


# escape дозволяє вивести рядок з тегами(екранізація тегів)
@app.route('/viewlog')
def view_the_logs() -> 'html':
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')

    return render_template('logs.html', the_row_titles=titles,
                           the_data=view_the_logs2(), the_title='View logs')



@app.route('/mylogs')
def view_my_logs() -> 'html':
    return render_template('my_logs.html',
                           log_data = view_logs3(), the_title='Welcome to my_logs')


@app.route('/dblogs2', methods = ['POST'] )
def view_bd_logs2() -> 'html':
    #app.secret_key = 'YouWillNeverGuessMySecretKey'
    user_name = request.form['user_name']
    login = request.form['login']

    if user_name == 'adminAdmin' and login == app.secret_key:

        titles = ('Id','Data','Phrase','Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('logs_from_bd.html', the_row_titles=titles,
                               log_data = read_from_db(SQL4), the_title='Welcome to bd_logs')

    return redirect('/entry')



@app.route('/loginDb', methods=['GET', 'POST'])
def do_login_book_version() -> 'html':
    title = "Please log in to see this pages"

    if request.method == 'POST':
        secret_code = request.form.get('secret_code')
        phrase = "Incorrect secret code. Please try again."

        if secret_code == app.secret_key:  # перевірка введеного коду
            session['logged_in'] = True
            return  redirect('/dblogs33')
        else:
            return render_template('login.html', the_phrase = phrase, the_title = title)
    return render_template('login.html', the_title = title)  # сторінка з формою


@app.route('/dblogs33')
@checker_loger_in
def view_bd_logs_with_decorator() -> 'html':
    titles = ('Id', 'Data', 'Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('logs_from_bd.html', the_row_titles=titles,
                           log_data=read_from_db(SQL4), the_title='Welcome to bd_logs')



@app.route('/dblogs')
def view_bd_logs() -> 'html':
    #return render_template('security_log.html')
    title = "Please log in to see this pages"
    return render_template('login.html',the_title = title)





if __name__ == '__main__':
    app.run(debug=True)

