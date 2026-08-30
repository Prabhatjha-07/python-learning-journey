import datetime

import pytz

# d = datetime.date(2020 , 5 , 3)
# print(d)

# tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(tday.weekday())
# print(tday.isoweekday())

# tdelta = datetime.timedelta(days = 7)
# print(tday + tdelta)
# print(tday - tdelta)

# bday = datetime.date(2026, 2 , 7)
# till_bday = tday - bday  
# print(till_bday)
# print(till_bday.total_seconds())

# t = datetime.time(9 ,45,34,1000)
# print(t)

# h = datetime.datetime(2023 , 2 , 23 , 12, 45 , 10, 10000)
# r = datetime.datetime(2026 , 8 , 25 , 3 , 45 , 30 ,20000 , tzinfo= datetime.timezone.utc)
# print(h)
# print(r)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_now)
# print(dt_today)
# print(dt_utcnow)

# for tz in pytz.all_timezones:
#     print(tz)
dt_mtn = datetime.datetime.now(tz= pytz.timezone('pacific/chuuk'))

print(dt_mtn.strftime('%B %d , %Y'))


"""
DATETIME MODULE - QUICK NOTES
"""

import datetime
import pytz


# ---------------- DATE ----------------

# Create a date
d = datetime.date(2020, 5, 3)
print(d)

# Today's date
today = datetime.date.today()
print(today)

# Date attributes
print(today.year)
print(today.month)
print(today.day)

# Monday = 0, Sunday = 6
print(today.weekday())

# Monday = 1, Sunday = 7
print(today.isoweekday())


# ---------------- TIMEDELTA ----------------

# Add / subtract time
delta = datetime.timedelta(days=7)

print(today + delta)
print(today - delta)


# ---------------- TIME ----------------

# time(hour, minute, second, microsecond)
t = datetime.time(9, 45, 34, 1000)
print(t)

# hour        -> 0-23
# minute      -> 0-59
# second      -> 0-59
# microsecond -> 0-999999


# ---------------- DATETIME ----------------

# datetime(year, month, day, hour, minute, second, microsecond)
dt = datetime.datetime(2023, 2, 23, 12, 45, 10, 10000)
print(dt)

# 10000 here = microseconds, NOT seconds
# Seconds must be between 0 and 59.


# ---------------- CURRENT TIME ----------------

print(datetime.datetime.today())     # Local date + time
print(datetime.datetime.now())       # Local date + time
print(datetime.datetime.now(datetime.timezone.utc))  # UTC


# ---------------- TIMEZONE ----------------

# Using pytz
tz = pytz.timezone("Pacific/Chuuk")
dt_tz = datetime.datetime.now(tz)

print(dt_tz)


# ---------------- STRFTIME ----------------

# datetime -> string

print(dt_tz.strftime("%B %d, %Y"))

# Common codes:
# %Y -> Year       %m -> Month
# %d -> Day        %B -> Month name
# %A -> Weekday    %H -> Hour
# %M -> Minute     %S -> Second


# ---------------- STRPTIME ----------------

# string -> datetime

date_str = "25-08-2026"

dt = datetime.datetime.strptime(
    date_str,
    "%d-%m-%Y"
)

print(dt)


# ---------------- QUICK REVISION ----------------

# date()       -> Date only
# time()       -> Time only
# datetime()   -> Date + time
# timedelta()  -> Time difference
# strftime()   -> datetime -> string
# strptime()   -> string -> datetime
# pytz         -> Timezones