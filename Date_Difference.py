from datetime import datetime

date1 = datetime.now()
date2 = datetime(day=1, month=7, year=2021)

timedelta = date2 - date1
print(timedelta)
