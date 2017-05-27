# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, '')

from flask import Flask, url_for
from hr.models import db

app = Flask(__name__)

app.config.from_object('hr.config.DevelopmentConfig')

# Database
db.init_app(app)

# Jinja extensions
app.jinja_options['extensions'].extend([
    'jinja2.ext.do',
])

@app.context_processor
def static_processor():
    def static(filename):
        return url_for('static', filename=filename)
    return dict(static=static)


@app.context_processor
def period_processor():
    def next_period(year, month):
        month = month + 1
        if month > 12:
            month = month - 12
            year = year + 1
        return year, month

    def prev_period(year, month):
        month = month - 1
        if month < 1:
            month = month + 12
            year = year - 1
        return year, month

    return dict(next_period=next_period,
                prev_period=prev_period)

import hr.views
