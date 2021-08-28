import os

class Config(object):
    ORIGINS = ['*']
    SECRET_KEY = os.getenv("SECRET_KEY")

class DevelopConfig(Config):
    DEBUG = True
    PORT = 5000
    ENV = 'dev'
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False