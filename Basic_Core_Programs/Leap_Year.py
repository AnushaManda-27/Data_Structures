'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title: Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.'''

year = int(input("Enter a year:"))
if (len(str(year)) == 4):
    if (year % 4) == 0 and (year % 100) == 0 or (year % 400) == 0:
        print(year, "is leap year")
    else:
        print(year, "not a leap year")
else:
    print("Year should have 4 digits")
