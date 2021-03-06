# -*- coding: utf-8 -*-

from datetime import timedelta

from flask import render_template, url_for, redirect

from hr import app
from hr.models import db, Employee
from hr.forms import EmployeeForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employee")
def employee_list():
    employees = Employee.query.order_by(Employee.file_no)\
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
    return render_template('employee_form.html', form=form)

@app.route("/employee/<int:id>")
def employee_view(id):
    from hr.utils import fixed_records
    employee = Employee.query.get_or_404(id)
    records = fixed_records(employee.month_records(2016, 12), 2016, 12)
    return render_template('employee_view.html',
                           employee=employee,
                           records=records,
                           timedelta=timedelta)

@app.route("/employee/<id>/edit")
def employee_edit(id):
    pass
