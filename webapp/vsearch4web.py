from  flask import Flask, render_template, request
from werkzeug.utils import redirect
from markupsafe import escape
from constants.constants import log_file
from search.privat import get_exchange_rates
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
def get_exchange_privat_rates() -> str:
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=5"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        result = []
        for currency in data:
            if currency['ccy'] in ['USD', 'EUR']:  # тільки ці валюти
                result.append(
                    f"{currency['ccy']} => {currency['base_ccy']}: <br> <br> BUY = {currency['buy']}, SELL = {currency['sale']}")

        return "<br><br>".join(result)  # HTML-перехід на новий рядок

    else:
        return f"Помилка запиту: {response.status_code}"



# escape дозволяє вивести рядок з тегами(екранізація тегів)
@app.route('/viewlog')
def view_logs() -> str:

    with open(log_file) as file:
       read_content = file.readlines()

    #return escape(read_content)
    return "<br>".join(escape(str(line)) for line in read_content)



if __name__ == '__main__':
    app.run(debug=True)




#fafcff
# tan