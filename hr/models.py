# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AttendanceRecord(db.Model):
    __tablename__ = 'attendance_record'

    id = db.Column(db.Integer, primary_key=True)
    user_code = db.Colun(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, unique=True)
    bkp_type = db.Column(db.Integer, nullable=False)
    type_code = db.Column(db.Integer, nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.UnicodeText, unique=True)
    email = db.Column(db.UnicodeText, unique=True)

    def __repr__(self):
        return '<User %s>' % self.username
