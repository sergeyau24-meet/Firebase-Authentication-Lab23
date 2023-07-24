from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
# import firebase
# from collections.abc import Mapping



Config = {
  "apiKey": "AIzaSyBkTBj8PEQ83FmP_eZBK7Eg3UJHZ31ppOg",
  "authDomain": "[y2-lab1.firebaseapp.com](https://www.google.com/search?q=y2-lab1.firebaseapp.com)",
  "projectId": "[y2-lab1](https://www.google.com/search?q=y2-lab1)",
  "storageBucket": "[y2-lab1.appspot.com](https://www.google.com/search?q=y2-lab1.appspot.com)",
  "messagingSenderId": "[188468048440](https://www.google.com/search?q=188468048440)",
  "appId": "[1:188468048440:web:9ca00c7cb32172de712ccd](https://www.google.com/search?q=1%3A188468048440%3Aweb%3A9ca00c7cb32172de712ccd)",
  "databaseURL":"https://y2-lab1-default-rtdb.europe-west1.firebasedatabase.app/"
}
fb = pyrebase.initialize_app(Config)
auth = fb.auth()
db = fb.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'vadim'



error = ''
@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        except:
            error = 'Auth Failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        bio = request.form['bio']
        username = request.form['username']
        # 
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        try:
            
            # print("vadim1")
            user = {'name': name,'email': email, 'password' : password, 'username': username, 'bio': bio}
            UID = login_session['user']['localId']
            db.child('Users').child(UID).set(user)
            return redirect(url_for('add_tweet'))
        except:
            pass

    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    

    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)