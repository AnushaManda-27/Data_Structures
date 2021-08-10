

'''
@Author: Anusha Manda
@Date: 2021-08-08 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-08 18: 00: 30
@Title:Takes two lists and print common elements
'''  

# list1 = [1, 17, 48, 678, 10, 23]
# new_list = [2, 23, 44, 678, 10]
list1 = input("Enter elemets of firstlist separated by comma: ").split(',')
new_list = input("Enter elemets of second list separated by comma: ").split(',')
common_ele = []

def check_common(lf1, new):
    for i in list1:
        for k in new_list:
            if i == k:
                common_ele.append(i)
                
check_common(list1, new_list)
print(common_ele)
