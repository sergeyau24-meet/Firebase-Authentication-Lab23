from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
from collections.abc import Mapping



config = {
  "apiKey": "[AIzaSyBkTBj8PEQ83FmP_eZBK7Eg3UJHZ31ppOg](https://www.google.com/search?q=AIzaSyBkTBj8PEQ83FmP_eZBK7Eg3UJHZ31ppOg)",
  "authDomain": "[y2-lab1.firebaseapp.com](https://www.google.com/search?q=y2-lab1.firebaseapp.com)",
  "projectId": "[y2-lab1](https://www.google.com/search?q=y2-lab1)",
  "storageBucket": "[y2-lab1.appspot.com](https://www.google.com/search?q=y2-lab1.appspot.com)",
  "messagingSenderId": "[188468048440](https://www.google.com/search?q=188468048440)",
  "appId": "[1:188468048440:web:9ca00c7cb32172de712ccd](https://www.google.com/search?q=1%3A188468048440%3Aweb%3A9ca00c7cb32172de712ccd)"
}
fb = pyrebase.initialize_app(config)
auth = fb.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'vadim'



error = ''
@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = reques.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        except:
            error = 'Auth Failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = reques.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = 'Auth Failed'

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    

    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)