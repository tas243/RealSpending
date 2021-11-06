import mechanize

### Maybe used later to access the website and test data going into the website
# Won't happen until I can run app.py from this file

br = mechanize.Browser()
br.open("http://127.0.0.1:5000/")
br.select_form(nr=0)
br.form['first'] = 'Troy'
br.form['last'] = 'Smith'
br.form['username'] = 'tas243'
br.form['password'] = 'pass'
req = br.submit()