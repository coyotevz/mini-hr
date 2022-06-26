# -*- coding: utf-8 -*-

from hr import app

@app.cli.command()
def initdb():
    from hr.models import db
    db.create_all(app=app)
