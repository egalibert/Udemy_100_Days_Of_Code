from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "neonlight"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
