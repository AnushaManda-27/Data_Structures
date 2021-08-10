'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Takes list input and prints sum of elements in that list 
'''

from functools import reduce

import sys, re

def input_validation(inp):

    '''Function: input_validation function is defined to validate input given
    
        Function parameters: elements

        Return : None
    '''


    macthobj = re.compile(r'((((-)?\d+)(,?))+)').search(inp)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()

if __name__ == '__main__':
    elements = input("Enter elements separated by comma: ")
    input_validation(elements)
    elements = elements.split(',')
    sum = reduce(lambda x,y: int(x)+int(y), elements)
    print(sum)
