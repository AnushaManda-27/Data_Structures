from functools import reduce


'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Takes list input and gives multiples of each element 
'''

# ele = [9,2,3,4,3,5,6,6,9]
ele  = input("Enter a list of elements separated by comma: ").split(',')

multiples = list(map(lambda a:a*3, ele))
print(multiples)



#Cloning or making a copy of list
 #  using list comphrehension
l2 = [i for i in ele] 
print(l2)

#Using Slicing method:

first_copy = ele[0: ]
print(first_copy)

#Remove duplicate elements from a list

new_ele= []
for i in ele:
    if i not in new_ele:
        new_ele.append(i)
print(new_ele)

# takes two list and return true 
# if they have atleast one element common
list1 = [1,17,48,678,10,23]
new_list = [2,23,44,678,10]
def check_common(lf1,new):
    for i in list1:
        for j in new_list:
            if i==j:
                return True
    
print(check_common(list1,new_list))
    
# for i in list1:
#     if i in new_list:
#         print(True)                 



