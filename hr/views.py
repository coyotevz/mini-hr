# -*- coding: utf-8 -*-

from flask import render_template, url_for

from hr import app
from hr.models import db, Employee

@app.route("/")
def index():
    employees = Employee.query.order_by(Employee.file_no)\
                              .order_by(Employee.hire_date)
    return render_template("employee_list.html", employees=employees)
