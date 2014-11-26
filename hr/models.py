# -*- coding: utf-8 -*-

from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TimestampMixin(object):

    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now,
                         onupdate=datetime.now)


class AttendanceRecord(db.Model):
    __tablename__ = 'attendance_record'

    id = db.Column(db.Integer, primary_key=True)
    user_code = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, unique=True)
    bkp_type = db.Column(db.Integer, nullable=False)
    type_code = db.Column(db.Integer, nullable=False)


class Employee(db.Model, TimestampMixin):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.UnicodeText, nullable=False)
    last_name = db.Column(db.UnicodeText, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    cuil = db.Column(db.Unicode(11), nullable=False)
    user_code = db.Column(db.Integer)

    records = db.relationship(
        AttendanceRecord,
        primaryjoin=user_code == db.foreign(AttendanceRecord.user_code),
        backref='employee', lazy='dynamic'
    )


class Address(db.Model, TimestampMixin):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    address_type = db.Column(db.Unicode(50))
    line1 = db.Column(db.UnicodeText, nullable=False)
    line2 = db.Column(db.UnicodeText)
    city = db.Column(db.UnicodeText, nullable=False)
    postal_code = db.Column(db.Unicode(32))

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),
                            nullable=False)
    employee = db.relationship(Employee,
                               backref=db.backref('address', lazy='joined'))


class Phone(db.Model, TimestampMixin):
    __tablename__ = 'phone'

    id = db.Column(db.Integer, primary_key=True)
    phone_type = db.Column(db.Unicode(50))
    prefix = db.Column(db.Unicode(8))
    number = db.Column(db.UnicodeText, nullable=False)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),
                            nullable=False)
    employee = db.relationship(Employee,
                               backref=db.backref('phone', lazy='joined'))


class Email(db.Model, TimestampMixin):
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True)
    email_type = db.Column(db.Unicode(50))
    email = db.Column(db.UnicodeText, nullable=False)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),
                            nullable=False)
    employee = db.relationship(Employee,
                               backref=db.backref('email', lazy='joined'))


class ExtraField(db.Model, TimestampMixin):
    __tablename__ = 'extra_field'

    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Unicode(50), nullable=False)
    field_value = db.Column(db.UnicodeText, nullable=False)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),
                            nullable=False)
    employee = db.relationship(Employee,
                               backref=db.backref("extra_field",
                                                  lazy='joined'))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.UnicodeText, unique=True)
    email = db.Column(db.UnicodeText, unique=True)

    def __repr__(self):
        return '<User %s>' % self.username
