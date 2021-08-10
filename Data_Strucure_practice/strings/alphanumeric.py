

'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: sorting elements in a set in alphanumeric way
'''

str1 = input("Enter strings separated by comma: ").split(',')

str2 = (','.join(sorted(list(set(str1)))))
print(str2)
