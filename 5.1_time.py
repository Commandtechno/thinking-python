import time

t = time.time()

SEC = 1
MIN = SEC * 60
HOUR = MIN * 60
DAY = HOUR * 24

print("number of days", t // DAY)
print("hour", (t % DAY) // HOUR)
print("minute", (t % HOUR) // MIN)
print("second", (t % MIN) // SEC)
