def nextDate(oldDate):
    MONTH = 0
    DAY = 1
    YEAR = 2

    daysPerMonth = {
        1: 31,
        2: None,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31 
    }

    try:
        date = list(map(int,oldDate.split("/")))
    except ValueError:
        print("Invalid input for date, must input as MM/DD/YYYY")

    # Ensures that the date was entered as MM/DD/YYYY with all integers
    if len(date) != 3:
        return "Invalid input for date, must input as MM/DD/YYYY"
    if not isinstance(date[MONTH], int) or not isinstance(date[DAY], int) or not isinstance(date[YEAR], int):
        return "Invalid input for date, must input as MM/DD/YYYY"

    # Ensures that the year is within specifications
    if date[YEAR] < 1900 or date[YEAR] > 2099:
        return "Invalid year, must be between 1900 and 2099"
    
    # Checks if the specified year is a leap year or not
    daysPerMonth.update({2: leapYear(date[YEAR])})

    # Ensures that the entered month is possible
    if (date[MONTH] < 1 or date[MONTH] > 12):
        return "Invalid input for month, must input as MM/DD/YYYY"

    # Ensures that the entered day is possible
    if (date[DAY] < 1 or date[DAY] > daysPerMonth.get(date[MONTH])):
        return "Invalid input for day, must input as MM/DD/YYYY"

    # Increments the date by 1 day
    date[DAY] = date[DAY] + 1
    if (date[DAY] > daysPerMonth.get(date[MONTH])):
        date[MONTH] = date[MONTH] + 1
        date[DAY] = 1
        if date[MONTH] > 12:
            date[YEAR] = date[YEAR] + 1
            date[MONTH] = 1

    return '/'.join(map(str,date))

def leapYear(year):
    if year % 4 != 0:
        return 28
    elif year % 100 != 0:
        return 29
    elif year % 400 != 0:
        return 28
    else:
        return 29

if __name__ == "__main__":
    print(nextDate("2/29/2016"))
    pass