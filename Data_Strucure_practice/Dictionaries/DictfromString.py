
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Converting String to dictionary
'''

str = input("Enter a string: ")

dict = {}
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i]=1
for key in dict:
    print(key,':',dict[key])

