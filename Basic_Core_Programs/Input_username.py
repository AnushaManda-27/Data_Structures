''' 
@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title:User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P​ -> Take User Name as Input. ​ Ensure UserName has min 3 char
b. Logic​ -> Replace <<UserName>> with the proper name
c. O/P​ -> Print the String with User Name 
'''
import re
import sys


def input_validation(ip):
    macthobj = re.compile(r'[A-Za-z]{2,}').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be 3 or more Alphabets only")
        sys.exit()


if __name__ == '__main__':
    name = input("Enter Username (with minimum 3 letters): ").title()
    input_validation(name)
    print("Hello "+name+", How are you?")
