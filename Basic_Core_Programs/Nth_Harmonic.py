'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title: Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http: // users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.
'''
import sys,re

def input_validation(ip):
    macthobj = re.compile(r'(\d)+').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


if __name__ == '__main__':
    num_harmonic = input("Enter a number: ")
    input_validation(num_harmonic)
    print(num_harmonic)
    count = 1
    harmonic =0
    while (int(num_harmonic) != 0) and (count <= int(num_harmonic)):
        harmonic = 1/count + harmonic
        count += 1
    print(harmonic)

