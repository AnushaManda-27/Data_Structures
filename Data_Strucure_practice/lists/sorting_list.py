'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Takes list input and sort all elements in list 
'''

def sort(tup):
    '''
    Function : sorting function is defined to sort on the elements in given tuple

    Function Parameters: tup - tuple

    Return: tup
    '''
    tup.sort(key = lambda x: x[1])
    return tup

tup = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort(tup))
