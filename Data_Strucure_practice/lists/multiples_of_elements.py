from functools import reduce


'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Takes list input and gives multiples of each element 
'''


ele  = input("Enter a list of elements separated by comma: ").split(',')

multiples = list(map(lambda a:a*3, ele))
print(multiples)



#Cloning or making a copy of list
 #  using list comphrehension
l2 = [i for i in ele] 
print(l2)

               



