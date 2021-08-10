

'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Takes list input and gives smallest and largest ofall elements 
'''

from functools import reduce

ele  = input("Enter a list of elements separated by comma: ").split(',')

smallest = reduce(lambda smallest, current: smallest if int(smallest) < int(current) else current, ele)
largest = reduce(lambda largest, current: largest if int(largest) > int(current) else current, ele)
print(f'min:{smallest} max:{largest}')
