'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Soting (descending )items in list of tuples by converting thhem to dictionary  
'''

import operator

dict1 = {'a':4,'b':7,'c':2,'d':10}

dict2 = sorted(dict1.items(), key=operator.itemgetter(1))
print(dict2)
dict2 = dict(sorted(dict1.items(),
            key=operator.itemgetter(1),reverse=True))
print(dict2)
