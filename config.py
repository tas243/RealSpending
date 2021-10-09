class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "fre8f7gsfdano8"
    # maybe import secret module from python or use os.random

    DB_NAME = "production-db"
    DB_USERNAME = "Troy"
    DB_PASSWORD = "Smith"
    SESSION_COOKIE_SECURE = False