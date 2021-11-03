from config import dbchar, configlio
import psycopg2

def challenge():
    con = dbchar()
    query = "SELECT * FROM function.users WHERE username = 'tas243';"
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchone()
    con.close()
    return data

x = challenge()
print(x[2])