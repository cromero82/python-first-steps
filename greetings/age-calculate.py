import datetime

current_date = datetime.datetime.now().date()
date_born = datetime.datetime(1982, 1, 1).date()

years = (current_date - date_born).days / 365
# 41.71506...

years = int(years)
print("I'm " + str(years) + " years old")
