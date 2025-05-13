from flask import Flask, session

app = Flask(__name__)


@app.route('/login')
def do_login() -> str:
 session['logged_in'] = True
 return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') #  видалення з словника
    return 'You are now logged out.'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session: # ЯКщо ключ logged_in є в словнику
        return 'Logged in as ' #+ session['user']
    return 'You are not logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'



if __name__ == '__main__':
 app.run(debug=True)