# This requires `pip install business-calendar`


from collections import namedtuple
from itertools import groupby
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY

# holiday download
_url = "https://mozorg.cdn.mozilla.net/media/caldata/ArgentinaHolidays.ics"


wd_str = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo",
}

wd_int = dict((v, k) for k, v in wd_str.items())


worktime_spec = {
    0: (['8:30', '12:30'], ['16:00', '20:00']),
    1: (['8:30', '12:30'], ['16:00', '20:00']),
    2: (['8:30', '12:30'], ['16:00', '20:00']),
    3: (['8:30', '12:30'], ['16:00', '20:00']),
    4: (['8:30', '12:30'], ['16:00', '20:00']),
    5: (['9:00', '13:00'],),
}

Interval = namedtuple("Interval", "start end")
WorkPeriod = namedtuple("WorkPeriod", "day weekday start end")


TODAY = date.today()

startseq = TODAY+relativedelta(day=1)
endseq = TODAY+relativedelta(day=31)

month_workdays = rrule(DAILY, dtstart=startseq, until=endseq,
                       byweekday=worktime_spec.keys())

work_periods = []

for d in month_workdays:
    for wp in worktime_spec.get(d.weekday()):
        p = WorkPeriod(d.day, d.weekday(), wp[0], wp[1])
        work_periods.append(p)

def daygroup(item):
    return item.day, item.weekday

wd_len = max(map(len, wd_str.values()))
out_fmt1 = "{{:<{}}} {{:>2}}: {{:>5}} a {{:>5}}".format(wd_len)
out_fmt2 = " "*(wd_len+1+2+2) + "{:>5} a {:>5}"

for ((day, weekday), wp) in groupby(work_periods, daygroup):
    p = list(wp)
    print(out_fmt1.format(wd_str[weekday], day, p[0].start, p[0].end))
    for w in p[1:]:
        print(out_fmt2.format(w.start, w.end))
