# -*- coding: utf-8 -*-

from flask_script import Manager
from hr import app

manager = Manager(app)

@manager.command
def initdb():
    from hr.models import db
    db.create_all(app=app)


def main():
    manager.run()

if __name__ == '__main__':
    main()
