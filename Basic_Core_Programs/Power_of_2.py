'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title:Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.
d. O/P -> Print the year is a Leap Year or not.
'''

import re
import sys


def input_validation(ip):
    macthobj = re.compile(r'(\d)+').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


if __name__ == '__main__':
    number = input("Enter a number to find 2 power of it :")
    input_validation(number)
    count = 0
    power_of_two = 1

    while count < int(number):
        power_of_two = 2 * power_of_two
        count += 1
print(power_of_two)
