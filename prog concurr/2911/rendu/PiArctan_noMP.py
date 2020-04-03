# -*- coding: utf-8 -*-

import math
import random
import time

if __name__ == '__main__':
    start = time.time()

    somme = 0
    max = 100000

    for i in range(1, max):
        div = 1 + (((i-0.5)/max)*((i-0.5)/max))
        somme += (4/div)

    somme = 1/max * somme

    print(somme)
