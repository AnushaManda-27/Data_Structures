'''@Author: Anusha Manda
@Date: 05-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 05-08-2021 18: 00: 30
@Title: Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer .
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''

import random
import sys
import re


def input_validation(ip):
    macthobj = re.compile(r'(\d)+').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


heads = 0
tails = 0

if __name__ == '__main__':
    coin_flips = input("Enter number of coin flips:")
    input_validation(coin_flips)
    coin_flips = int(coin_flips)

    for flips in range(coin_flips):
        y = random.randint(0, 1)
        if y < 0.5:
            heads += 1
        else:
            tails += 1
    head_flips = (heads/coin_flips)*100
    tail_flips = (tails/coin_flips)*100
    print("Heads vs Tail percentage is: {}, {}".format(head_flips, tail_flips))
