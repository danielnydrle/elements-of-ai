import math
import random
import numpy as np
from io import StringIO
import numpy as np

import random as rand

def generate(p1):
    seq = ""
    for i in range (10000):
        rand_num = random.random()
        if rand_num < p1:
            seq += "1"
        else:
            seq += "0"
    print(seq)
    return seq

def count(seq):
    ct = 0
    for i in range(len(seq)-4):
        if seq[i:i+5] == "11111":
            ct += 1
        else:
            continue
    return ct

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))