"""
This is a simple python program that tells you whether it is a good day today.

Enjoy :D
"""

import random

def is_it_a_good_day():
    x = random.randint(0,1)
    if x == 1:
        print("Today is a good day! :)")
    else:
        print("Today is not so good day! :)")

if __name__ == "__main__":
    is_it_a_good_day()