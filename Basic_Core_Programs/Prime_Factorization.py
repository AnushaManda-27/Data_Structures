'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title:Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency .
d. O/P -> Print the prime factors of number N.
'''
import sys
import re


def input_validation(ip):
    macthobj = re.compile(r'(\d)+').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


def prime_numbers_upto(num):
    prime_number = []
    for i in range(1, num+1):
        count = 0
        for j in range(1, num+1):
            if i % j == 0:
                count += 1
            else:
                continue
        if count <= 2:
            prime_number.append(i)
    return prime_number


if __name__ == '__main__':
    number = input("Enter a number to find its prime factors: ")
    input_validation(number)
    number = int(number)
    total_primefactors = []
    prime_number = prime_numbers_upto(number)
    for i in prime_number:
        if number % i == 0:
            total_primefactors.append(i)
        else:
            continue
    print(total_primefactors)
