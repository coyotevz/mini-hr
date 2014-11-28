from collections import namedtuple, OrderedDict
from itertools import groupby
from datetime import datetime, time, date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY
from dateutil.parser import parse



Interval = namedtuple("Interval", "input output")

worktime_spec = {
    0: (['8:30', '12:30'], ['16:00', '20:00']),
    1: (['8:30', '12:30'], ['16:00', '20:00']),
    2: (['8:30', '12:30'], ['16:00', '20:00']),
    3: (['8:30', '12:30'], ['16:00', '20:00']),
    4: (['8:30', '12:30'], ['16:00', '20:00']),
    5: (['9:00', '13:00'],),
}

def perfect_grid(year, month):
    sdate = date(year, month, 1)
    edate = sdate+relativedelta(day=31)

    workdays = rrule(DAILY, dtstart=sdate, until=edate,
                     byweekday=worktime_spec.keys())

    grid = [(day.date(),
             [Interval(parse(i[0]).time(), parse(i[1]).time())\
              for i in worktime_spec.get(day.weekday())])\
            for day in workdays]
    return grid


def time_diff(t1, t2):
    t1_sec = (t1.hour*60+t1.minute)*60+t1.second
    t2_sec = (t2.hour*60+t2.minute)*60+t2.second
    return timedelta(seconds=t1_sec-t2_sec)

def _gdate(item):
    return item.datetime.date()

RDiff = namedtuple("RDiff", "orig diffs")

def fixed_records(query, year, month):
    grid = perfect_grid(year, month)

    records = dict((day, [r.datetime.time() for r in record])\
                    for day, record in groupby(query, _gdate))

    fixed = []
    for day, intervals in grid:
        day_records = records.get(day, [])
        for i in intervals:
            f = Interval(
                RDiff(i[0], [(r, time_diff(r, i[0])) for r in day_records]),
                RDiff(i[1], [(r, time_diff(r, i[1])) for r in day_records]),
            )
            print(f)
