from hr.models import Employee
from hr.utils import fixed_records
from datetime import datetime, timedelta
from tabulate import tabulate

def employee_report(employee_id, year, month):
    employee = Employee.query.get(employee_id)
    if not employee:
        print(f"No employee found with id={employee_id}")
        return
    records = fixed_records(employee.month_records(year, month), year, month)
    report = []
    for (day, intervals) in records:
        for interval in intervals:
            report.append((
                *day.strftime("%d %A").title().split(),
                interval.input,
                interval.output
            ))
    print(tabulate(report,
        #headers=["Fecha", "Día", "Entrada", "Salida"],
        tablefmt="plain")
    )
