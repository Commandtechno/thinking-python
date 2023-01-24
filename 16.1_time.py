"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """


def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def mul_time(time, distance):
    return int_to_time(time_to_int(time) * distance)


def pace(finishing_time, miles):
    # divide
    return mul_time(finishing_time, 1 / miles)


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 0
    noon_time.minute = 15
    noon_time.second = 0

    print_time(pace(noon_time, 15))


if __name__ == "__main__":
    main()
