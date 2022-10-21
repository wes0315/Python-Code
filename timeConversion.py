# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
s0 = '12:45:54PM'


def timeConversion(s):
    if s[8: 10] == 'PM':
        PM = format(int(s[0:2]), "02d")
        if int(PM) == 12:
            pass
        else:
            new_PM = int(PM)+12
            s = s.replace(str(PM), str(new_PM))
    else:
        AM = format(int(s[0:2]), "02d")
        AM = int(AM)
        if AM == 12:
            new_AM = format(AM-12, "02d")
            s = s.replace(str(AM), str(new_AM))
        else:
            pass
    return s[:8]


print(timeConversion(s0))
