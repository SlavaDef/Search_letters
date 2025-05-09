import html

from  flask import Flask, render_template, request
from werkzeug.utils import redirect
from markupsafe import escape
from constants.constants import log_file
from search.privat import get_exchange_rates, get_exchange
from search.search_letters import find_letters_in_words, find_letters_in_words_version_second
import requests

from search.write import directory, write_message, log_request, reading_log_file

app = Flask(__name__)

#@app.route('/')
#def hello() -> '302':
  #  return redirect('/entry')


@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are you results'
    results = str(find_letters_in_words_version_second(phrase,letters))
    currency_res = get_exchange_rates() # курси валют
    write_message(phrase, letters, results) # запис логів, данних про вводи
    log_request(request,results) # book version
    return render_template('results.html', the_phrase = phrase, the_letters = letters,
                           the_title = title, the_results= results, the_currency_res = currency_res )



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search4letters on the web!')




@app.route('/privat')
def get_exchange_privat_rates() -> html:
     return render_template('privat.html', the_title = 'Exchange_rates', pr_data=get_exchange())


# escape дозволяє вивести рядок з тегами(екранізація тегів)
@app.route('/viewlog')
def view_logs_my_vers() -> 'html':
    res = []
    with open(log_file) as file:
        content = file.readlines()
        for line in content:
            o = line.split("***")
            res.append(o)
    escape(str(res))

    return render_template('logs.html', log_data=res, the_title='View logs')

   #return "<br>".join(escape(str(line)) for line in read_content)


@app.route('/mylogs')
def view_my_logs() -> 'html':
    res=[]
    with open(directory) as file:
        read_all = file.readlines()
        for line in read_all:
            res.append(line.split("*"))

    return render_template('my_logs.html', log_data = res, the_title='Welcome to my_logs')
    #return "<br>".join(str(line) for line in read_all)




if __name__ == '__main__':
    app.run(debug=True)

