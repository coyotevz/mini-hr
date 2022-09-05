# -*- coding: utf-8 -*-

import click
from hr import app

@app.cli.command()
def initdb():
    "Initialize empty database."
    from hr.models import db
    db.create_all(app=app)


@app.cli.command()
@click.argument("employee_id")
@click.argument("year", required=False)
@click.argument("month", required=False)
def report_employee(employee_id, year=None, month=None):
    """
    Write out employee records report.

    \b
    EMPLOYEE_ID for employee to report.
    YEAR of report period [DEFAULT: current year].
    MONTH of report period [DEFAULT: last month].
    """
    from datetime import datetime, timedelta
    last_period = datetime.today() - timedelta(days=30)
    if year is None:
        year = last_period.year
    if month is None:
        month = last_period.month
    from hr.reports import employee_report
    employee_report(employee_id, year, month)
