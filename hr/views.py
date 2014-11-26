# -*- coding: utf-8 -*-

from flask import render_template, url_for

from hr import app
from hr.models import db

@app.route("/")
def index():
    return render_template("index.html")
