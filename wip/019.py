daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if (year % 100) == 0 and (year % 400) != 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

def dayOfTheWeek(month, day, year):
    days = 0
    for i in range(1970, year):
        if isLeapYear(i) == True:
            days += 366
        else:
            days += 365
    for i in range(month-1):
        days += daysInMonths[i]
    if isLeapYear(year):
        days += 1
    days += day - 1
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[(days+3) % 7]

count = 0
for years in range(1901, 2001):
    for months in range(1, 13):
        if dayOfTheWeek(months, 1, years) == "Sunday":
            count += 1
print(count)