# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600


def make_readable(seconds):
    hours, rem = divmod(seconds, SECONDS_PER_HOUR)
    minutes_part, seconds_part = divmod(rem, SECONDS_PER_MINUTE)

    return "{:02}:{:02}:{:02}".format(hours, minutes_part, seconds_part)

# Again what learned:
# You can format strings this way
# f"{hours:02d}:{minutes:02d}:{seconds:02d}"
