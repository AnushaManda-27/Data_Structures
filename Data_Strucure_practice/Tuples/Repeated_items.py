

'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Printing repeated elements in a tuple
'''

tup = ('a','n','u','s','h','a','m','a','n','d','a')
tup1 = []

for i in tup:
    #print(tup.count(i))
    if tup.count(i) > 1:
        tup1.append(i)
print(tup1)
