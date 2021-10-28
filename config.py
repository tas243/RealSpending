import psycopg2

def dbchar():
    bd = {
        'user': 'postgres',
        'pw': 'Rootwjzs16',
        'host': 'localhost',
        'db': 'var_inputs'
    }
    cons = psycopg2.connect(user=bd['user'],
        password=bd['pw'],
        host=bd['host'],
        database=bd['db'])
    
    return cons

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "fre8f7gsfdano8"
    # maybe import secret module from python or use os.random