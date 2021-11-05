import psycopg2
from config import dbchar
##### Still some problems with integrating in line 90: if db_uservalue != username_value:
# NameError: name 'db_uservalue' is not defined
def search_user(username_value,valuefinder):
    values = ['pk', 'first', 'last', 'username', 'password', 'date']
    finder = []
    st = ''
    for value in valuefinder:
        if value in values:
            for i,j in enumerate(values):
                if value == j:
                    finder.append(value)
                    st += "%s," % j
        else:
            print('"' + value + '"'  + ' is not a query tool')
    length = len(st)
    s = st[0:length-1]
    
    con = dbchar()
    query = "SELECT %s FROM function.users WHERE username = '%s';" % (s, username_value)
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchone()
    return data
    con.close()

valuefinder = ['username','password','first']
username_value = 'tas243'
user = search_user(username_value,valuefinder)
print(user)