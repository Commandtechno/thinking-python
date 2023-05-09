import time


SEC = 1
MIN = SEC * 60
HOUR = MIN * 60
DAY = HOUR * 24


def display_time(s):
    print("number of days", s // DAY)
    print("hour", (s % DAY) // HOUR)
    print("minute", (s % HOUR) // MIN)
    print("second", (s % MIN) // SEC)


now = time.time()
lnow = time.localtime()
print("-", "now")
print("hour", lnow.tm_hour)
print("minute", lnow.tm_min)
print("second", lnow.tm_sec)
print("month", lnow.tm_mon)
print("year", lnow.tm_year)
print()

christmas = time.mktime((lnow.tm_year, 12, 25, 0, 0, 0, 0, 0, 0))
print("-", "time till christmas")
display_time(christmas - now)
print()
