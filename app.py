from flask import Flask, render_template, redirect, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import datetime
from pytz import timezone
from config import dbchar, configlio

app = Flask(__name__)

# env\Scripts\activate.ps1 inserting this into powershell activates virtual environment

# Configuring Flask and database
conf = configlio()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost/%s' % (conf.get('pw'), conf.get('db'))
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# Create a function to open connection and cursor
# Create a function to close both

# con = dbchar()
# close con (connection)?
# If you want to open the cursor, type the following line
# cur = con.cursor()

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

    @classmethod
    def signup_username_check(self,username_value,valuefinder):
        ### Maybe add a parameter for if you are looking for a specific attribute, that is input and turned into the location in the tuple
        values = ['pk', 'firstname', 'lastname', 'username', 'password', 'date']
        finder = 0
        if valuefinder in values:
            for i,j in enumerate(values):
                if valuefinder == j:
                    finder = i
        print(finder)
        con = dbchar()
        query = "SELECT * FROM function.users WHERE username = '%s';" % username_value
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return data[finder]
        con.close()
        # data is a tuple of the users in database

@app.route('/', methods = ["POST", "GET"])
def signup():
    title = "Welcome! please feel free to create an account."
    if request.method   ==  "POST":
        req             =   request.form
        # return jsonify(req)
        # create a javascript object by uncommenting the above line
        first_value     =   req['first']
        last_value      =   req['last']
        username_value  =   req['username']
        passw_value     =   req['password']
        new_user        =   users(first=first_value, last=last_value, username=username_value, password=passw_value)
        # This calls the class method to check if the username is taken
        user = users()
        db_uservalues = user.signup_username_check(username_value,'username')
        if db_uservalue != username_value:
            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                return "Nice Try"
        else:
            # Ask for a new username, since username is already taken
            return "Username Taken"
        
    else:
        return render_template('signup.html', title=title)

# @app.route('/transactions', methods=["POST", "GET"])
# def transactions():
#     title = "Input your transactions"
#     if request.method   ==  "POST":
#         amount_value    =   request.form['amount']
#         category_value  =   request.form['category']
#         new_row         =   transactions(amount=amount_value, category=category_value)
#         # push to database
#         try:
#             db.session.add(new_row)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an error, NICE"
#     else:
#         return render_template('entry.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)