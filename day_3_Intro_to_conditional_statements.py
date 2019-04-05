#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

if N%2 != 0: # if N is odd print Weird
    print("Weird")
elif (N%2 == 0) and (6 <= N <=20): # if N is even and is in the range 6-20 print Weird
    print("Weird")
elif (N%2 == 0) and (20 < N <= 100): # if N is even and is in the range 20-100 print Not Weird
    print("Not Weird")
else:
    print("Not Weird") # if N is even print Not Weird, and for all other cases