from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

inputs = []

# env\Scripts\activate.ps1 inserting this into powershell activates virtual environment

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Rootwjzs16@localhost/var_inputs'
app.config.from_object('config.Config')

db = SQLAlchemy(app)

#Create db model
class transactions(db.Model):
    __tablename__   =   "transactions"
    __table_args__  =   {'schema':'function'}
    tz              =   timezone('EST')
    date2           =   datetime.now(tz)
    id              =   db.Column(db.Integer, primary_key=True)
    amount          =   db.Column(db.Integer, nullable=False)
    date            =   db.Column(db.DateTime, default=date2, nullable=False)
    category        =   db.Column(db.String(30), nullable=False)

class users(db.Model):
    __tablename__   =   "users"
    __table_args__  =   {'schema':'function'}
    tz              =   timezone('EST')
    date3           =   datetime.now(tz)
    id              =   db.Column(db.Integer, primary_key=True)
    first           =   db.Column(db.String(30), nullable=False)
    last            =   db.Column(db.String(30), nullable=False)
    username        =   db.Column(db.String(30), nullable=False, unique=True)
    password        =   db.Column(db.String(30), nullable=False)
    date            =   db.Column(db.DateTime, default=date3, nullable=False)

@app.route('/', methods = ["POST", "GET"])
def signup():
    title = "Welcome! please feel free to create an account."
    if request.method   ==  "POST":
        first_value     =   request.form['first']
        last_value      =   request.form['last']
        username_value  =   request.form['username']
        passw_value     =   request.form['password']
        new_user        =   users(first=first_value, last=last_value, username=username_value, password=passw_value)
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return "Nice try"
    else:
        return render_template('signup.html', title=title)

#@app.route('/login', methods = ["POST", "GET"])
#def login():
#    title = "Welcome, please log in."
#    if request.method   ==  "POST":
#        username        =   request.form['username']
#        passw           =   request.form['password']

@app.route('/transactions', methods=["POST", "GET"])
def transactions():
    title = "Input your transactions"
    if request.method   ==  "POST":
        amount_value    =   request.form['amount']
        category_value  =   request.form['category']
        new_row         =   transactions(amount=amount_value, category=category_value)

        # push to database
        try:
            db.session.add(new_row)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error, NICE"
    else:
        return render_template('entry.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)