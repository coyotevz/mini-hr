# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, '')

from flask import Flask, url_for
from hr.models import db

app = Flask(__name__)

app.config.from_object('hr.config.DevelopmentConfig')

# Database
db.init_app(app)

@app.context_processor
def static_processor():
    def static(filename):
        return url_for('static', filename=filename)
    return dict(static=static)

import hr.views
