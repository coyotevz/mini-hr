# -*- coding: utf-8 -*-

from datetime import timedelta, date

from flask import render_template, url_for, redirect, request

from hr import app
from hr.models import db, Employee
from hr.forms import EmployeeForm
from hr.utils import fixed_records

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employee")
def employee_list():
    employees = Employee.query.filter(Employee.is_active==True)\
                              .order_by(Employee.file_no)\
                              .order_by(Employee.hire_date)
    return render_template('employee_list.html', employees=employees)

@app.route("/employee/add", methods=['GET', 'POST'])
def employee_add():
    form = EmployeeForm()
    if form.validate_on_submit():
        e = Employee()
        form.populate_obj(e)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('employee_list'))
    print(form.errors)
    return render_template('employee_form.html', form=form)

@app.route("/employee/<int:id>")
def employee_view(id):
    period = request.args.get('period', None)
    today = date.today()
    if period is None:
        year, month = today.year, today.month
    else:
        year, month = int(period[:4]), int(period[4:])
    employee = Employee.query.get_or_404(id)
    records = fixed_records(employee.month_records(year, month), year, month)
    return render_template('employee_view.html',
                           employee=employee,
                           records=records,
                           year=year,
                           month=month,
                           timedelta=timedelta)

@app.route("/employee/<id>/edit")
def employee_edit(id):
    pass
