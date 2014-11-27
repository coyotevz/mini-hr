# -*- coding: utf-8 -*-

from flask import render_template, url_for

from hr import app
from hr.models import db, Employee

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employee")
def employee_list():
    employees = Employee.query.order_by(Employee.file_no)\
                              .order_by(Employee.hire_date)
    return render_template("employee_list.html", employees=employees)

@app.route("/employee/add")
def employee_add():
    pass

@app.route("/employee/<id>")
def employee_view(id):
    pass

@app.route("/employee/<id>/edit")
def employee_edit(id):
    pass
