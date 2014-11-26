# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.UnicodeText, unique=True)
    email = db.Column(db.UnicodeText, unique=True)

    def __repr__(self):
        return '<User %s>' % self.username
