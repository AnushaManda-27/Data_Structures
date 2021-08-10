
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Using Frozen sets as Keys in a dictionary and
        some operations performed on frozensets
'''

person = {'name':'Anusha', 'age':23, 'gender':'female'}
set = frozenset(person)
print(set)

# operation performed on frozensets

seta = frozenset([1,2,3,4,5])
setb = frozenset([4,5,6,7,8])
setc = frozenset([3,4])

print(seta.isdisjoint(setb))
print(setc.issubset(seta))
print(seta.issuperset(setc))
