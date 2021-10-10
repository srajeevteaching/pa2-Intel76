# Hanna Magan
# Course: CS151-02, Dr. Rajeev
# Date: 10/4/21
# Programming Assignment: 2
# Program Inputs: Month (1-12) and year
# Program Outputs: Number of days in the month

month = input("Input month (1-12):")
year = input("Input year")
leapYear = False

#Program calculates if the year is a leap year.
if year % 4 == 0:
    leapYear = True
#Program calculates if the year is a leap year.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(" 31 days .")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days .")
elif month == 2 and year % 4:
    print(" 29 days.")
elif month == 2 and not year % 4:
    print("28 days in month.")
