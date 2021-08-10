
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Coverting a string to dictionary(keys as elements and values as their count)
'''

str1 = input("Enter a string: ")
dict = {}
for i in str1:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)


