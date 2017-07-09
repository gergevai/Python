# Project : Create a program that, when given a date, displays the name of the day on that specific date.
# Formula and information found on: "https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week"
# Program verified with: "http://www.calculatorcat.com/free_calculators/day_of_week.phtml"
# Program determines day of dates according to the Gregorian Calendar.
# Gregorian dates before 1500-1600 theoretically do not exist, as the Julian calendar was still in use.

# ========== Functions ==========


def determine_century(cent):  # Century code.
    if cent % 4 == 3:  # 15 , 19 , 23 etc.
        return 1
    elif cent % 4 == 0:  # 16 , 20 , 24 etc.
        return 0
    elif cent % 4 == 2:  # 18 , 22 , 26 etc.
        return 3
    elif cent % 4 == 1:  # 17 , 21 , 25 etc.
        return 5


def determine_month(mon, le):  # Month code.
    if mon == 1:
        if le == 0:  # Not leap year
            return 0
        else:  # Leap year.
            return 6
    elif mon == 2:
        if le == 0:  # Not leap year.
            return 3
        else:  # Leap year.
            return 2
    elif mon == 3:
        return 3
    elif mon == 4:
        return 6
    elif mon == 5:
        return 1
    elif mon == 6:
        return 4
    elif mon == 7:
        return 6
    elif mon == 8:
        return 2
    elif mon == 9:
        return 5
    elif mon == 10:
        return 0
    elif mon == 11:
        return 3
    elif mon == 12:
        return 5


def determine_day(d):  # Day code.
    if d == 0:
        return 'Saturday'
    elif d == 1:
        return 'Sunday'
    elif d == 2:
        return 'Monday'
    elif d == 3:
        return 'Tuesday'
    elif d == 4:
        return 'Wednesday'
    elif d == 5:
        return 'Thursday'
    elif d == 6:
        return 'Friday'


def determine_if_leap(yr):  # Check for leap year.
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
        return 1
    else:
        return 0


def check_date(d, m, y):
    if d < 0 or d > 31:
        return False
    if m < 0 or m > 12:
        return False
    if y < 0:
        return False
    return True

# ========== Main body ==========

# ========== Input ==========
day = int(raw_input("Give the number of the day:"))
month = int(raw_input("Give the number of the month:"))
year = raw_input("Give the number of the year:")

while not check_date(day, month, year):
    print "Please re-enter a correct date"
    day = int(raw_input("Give the number of the day:"))
    month = int(raw_input("Give the number of the month:"))
    year = raw_input("Give the number of the year:")

# ========== Create data ==========
century = int(year[0:2])  # Take century
yeardigit = int(year[2:4])  # Find last 2 digits of year.
year = int(year)  # Cast to int.
centcode = determine_century(century)  # Find century code.
leap = determine_if_leap(year)  # Leap year?
monthcode = determine_month(month, leap)  # Find month code.
Formula = (day + monthcode + yeardigit + yeardigit / 4 + centcode) % 7
# Formula : daycode = (day + monthcode + yeardigits + yeardigits/4 + centurycode) mod 7
dayname = determine_day(Formula)  # Find day code.
print "\nGiven date:", day, "/", month, "/", year
print "\nDay of the week:", dayname
