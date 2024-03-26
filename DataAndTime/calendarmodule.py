import calendar
m, d, y = map(int, input().split())
finaldate = str(d) + " " + str(m) + " " + str(y)

def dateFunction(finaldate):
    day, month, year = (int(i) for i in finaldate.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[dayNumber].upper()

print(dateFunction(finaldate))

"""
input
08 05 2015

output
WEDNESDAY
"""
