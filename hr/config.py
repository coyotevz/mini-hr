# -*- coding: utf-8 -*-

from os import path

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '<must be secret>' # use os.urandom(24) to generate this

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' %\
        path.join(path.abspath(path.curdir), 'data_hr.db')
