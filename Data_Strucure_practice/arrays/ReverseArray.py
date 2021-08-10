
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Reversing elements in an array an printing them
'''

import array as ar

array = ar.array('i', [1, 2, 3, 4, 5])
array.reverse()
print(array)
for i in range(len(array)):
    print(array[i])
