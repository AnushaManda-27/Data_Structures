
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Finding difference, symmetric difference between two sets
'''

set1 = {20, 30, 40, 50, 60, 70}
set2 = {10, 20, 30, 40, 80, 90}

set3 = set1.difference(set2)
print(set3)

#symmetric difference

set4 = set1.symmetric_difference(set2)
print(set4)


