## Test on how to change definitions once the user creates a login/signs in

from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def signup():
    title = "Welcome! please feel free to create an account."
    if request.method   ==  "POST":
        req             =   request.form
        # return jsonify(req)
        # create a javascript object by uncommenting the above line
        username_value  =   req['username']
        transactions(username_value)
    else:
        return render_template('signup.html', title=title)

@app.route('/transactions', methods=["POST", "GET"])
def transactions(username_value):
    title = 'Enter a transaction %s' % username_value
    return render_template('entry.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)