'''
@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title:Sum of three Integer adds to ZERO
a. Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second output is to
print the distinct triplets.
'''
import sys
import re


def input_validation(ip):
    macthobj = re.compile(r'((((-)?\d+),?)+)').search(ip)
5400 15 05+ if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


def sum_of_three(array, array_length):
    '''Description:
            sum_of_three function is defined to identify unique triplets whose sum is zero
        Function PArameters:
            array, array_length
        Return:
            None
    '''
    global count
    for i in range(0, array_length-2):
        for j in range(i+1, array_length-1):
            for k in range(j+1, array_length):
                if (int(array[i])+int(array[j])+int(array[k])) == 0:
                    count += 1
                    print(array[i]+" "+array[j]+" "+array[k])
                    break
                else:
                    continue
    print("no of triplets:-{}".format(count))


if __name__ == '__main__':
    array = input("Enter integers separated by ',': ")
    input_validation(array)
    array = array.split(",")
    array_length = len(array)
    count = 0
    print("array : ", array)
    sum_of_three(array, array_length)
