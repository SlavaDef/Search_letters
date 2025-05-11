import html
import os

from  flask import Flask, render_template, request
from werkzeug.utils import redirect
from markupsafe import escape
from user_agents import parse

from service.dbWrite import write_db, read_all_from_db, read_all_from_db2
from service.logs import view_logs, view_logs2, view_logs3, view_the_logs2
from utils.constants import log_file
from service.privat import get_exchange_rates, get_exchange
from service.search_letters import find_letters_in_words, find_letters_in_words_version_second
import requests

from service.write import directory, write_message, log_request, reading_log_file

# Отримаємо абсолютний шлях до каталогу webapp/
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'webapp'))

app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

#@app.route('/')
#def hello() -> '302':
  #  return redirect('/entry')


#app.config['dbconfig'] = {'host': '127.0.0.1','user': 'vsearch','password': 'vsearchpasswd','database': 'vsearchlogDB', }



@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    remote = str(request.remote_addr)

    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    browser = user_agent.browser.family

    title = 'Here are you results'
    results = str(find_letters_in_words_version_second(phrase,letters))
    write_db(phrase, letters, remote, browser, results)
    currency_res = get_exchange_rates() # курси валют
    write_message(phrase, letters, results) # запис  данних про вводи, my wersion
    log_request(request,results) # book version
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


@app.route('/dblogs')
def view_bd_logs() -> 'html':
    titles = ('Id','Data','Phrase','Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('logs_from_bd.html', the_row_titles=titles,
                           log_data = read_all_from_db2(), the_title='Welcome to bd_logs')


if __name__ == '__main__':
    app.run(debug=True)

