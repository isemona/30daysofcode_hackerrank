#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    # write to handle to arry input

    a = list(input().rstrip().split())
    print(' '.join(reversed(a)))

