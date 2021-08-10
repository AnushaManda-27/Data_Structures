
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Returning the longest element in list
'''

list1 = ["restart","return","system","computer"]
list2 = []

for i in list1:
    list2.append((len(i), i))
list2.sort()
print(list2[-1][1], len(list2[-1][1]))


