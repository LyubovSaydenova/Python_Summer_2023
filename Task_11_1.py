from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta, TH
def output(data):
    new_date = data + relativedelta(day=1, weekday=TH(3))
    if new_date <= data:
        new_date = data + relativedelta(months=+1, day=1, weekday=TH(3))
    print(new_date)
    return (new_date - data).days
dt = input()
dt = date(*map(int, dt.split('-')))
print(output(dt))