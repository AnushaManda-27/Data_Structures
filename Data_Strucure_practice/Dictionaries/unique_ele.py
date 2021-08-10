
'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Printing unique items present in a dictionary
'''


list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

s = set() #cause set has no duplication
for dict in list_dict:
   for value in dict.values():
      s.add(value)
print(s)
