from datetime import datetime    #first setting datetime to be a reference to the class, then immediately setting it to be a reference to the module.

date1 = datetime.now()
date2 = datetime(day=1, month=7, year=2021)

timedelta = date2 - date1
print(timedelta)
